import imp
from rest_framework.serializers import ValidationError
from django.http import HttpResponsePermanentRedirect
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import viewsets, generics, status, permissions
from rest_framework.mixins import CreateModelMixin, UpdateModelMixin, DestroyModelMixin
from authentication.serializers import InstitutionSerializer, LoginSerializer, LoginUserSerializer, LogoutSerializer, ResetPasswordEmailRequestSerializer, SetNewPasswordSerializer
from authentication.models import Institution
from authentication.utils import Util
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from rest_framework.exceptions import AuthenticationFailed
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import smart_str, force_str, smart_bytes, DjangoUnicodeDecodeError
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
import os


class InstitutionViewSet(CreateModelMixin, DestroyModelMixin,
                         viewsets.GenericViewSet):
    serializer_class = InstitutionSerializer
    queryset = Institution.objects.all()



class LoginAPIView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=self.request.data)
        serializer.is_valid(raise_exception=True)

        username = serializer.validated_data.get('username')
        password = serializer.validated_data.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
        else:
            raise AuthenticationFailed('Username or Password is not valid !')

        token = Token.objects.get_or_create(user=user)[0]
        return Response(LoginUserSerializer(user).data,
                        status=status.HTTP_200_OK)


class RequestPasswordResetEmail(generics.GenericAPIView):
    serializer_class = ResetPasswordEmailRequestSerializer

    def post(self, request):
        serializer = self.serializer_class(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data.get('email')
        redirect_url = serializer.validated_data.get('redirect_url')

        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)
            uidb64 = urlsafe_base64_encode(smart_bytes(user.id))
            token = PasswordResetTokenGenerator().make_token(user)
            current_site = get_current_site(request=request).domain
            relativeLink = f'password-reset/<{uidb64}>/<{token}>/'

            absurl = 'http://' + current_site + relativeLink
            email_body = 'Hello, \n Use link below to reset your password  \n' + \
                absurl+"?redirect_url="+redirect_url
            data = {
                'email_body': email_body,
                'to_email': user.email,
                'email_subject': 'Reset your passsword'
            }
            Util.send_email(data)
        return Response(
            {'success': 'We have sent you a link to reset your password'},
            status=status.HTTP_200_OK)


class PasswordTokenCheckAPI(generics.GenericAPIView):
    serializer_class = SetNewPasswordSerializer

    def get(self, request, uidb64, token):

        redirect_url = request.GET.get('redirect_url')

        try:
            id = smart_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(id=id)

            if not PasswordResetTokenGenerator().check_token(user, token):
                if len(redirect_url) > 3:
                    return HttpResponsePermanentRedirect(redirect_url +
                                                         '?token_valid=False')
                else:
                    return HttpResponsePermanentRedirect(
                        os.environ.get('FRONTEND_URL', '') +
                        '?token_valid=False')

            if redirect_url and len(redirect_url) > 3:
                return HttpResponsePermanentRedirect(
                    redirect_url +
                    '?token_valid=True&message=Credentials Valid&uidb64=' +
                    uidb64 + '&token=' + token)
            else:
                return HttpResponsePermanentRedirect(
                    os.environ.get('FRONTEND_URL', '') + '?token_valid=False')

        except DjangoUnicodeDecodeError as identifier:
            try:
                if not PasswordResetTokenGenerator().check_token(user):
                    return HttpResponsePermanentRedirect(redirect_url +
                                                         '?token_valid=False')

            except UnboundLocalError as e:
                return Response(
                    {'error': 'Token is not valid, please request a new one'},
                    status=status.HTTP_400_BAD_REQUEST)


class SetNewPasswordAPIView(generics.GenericAPIView):
    serializer_class = SetNewPasswordSerializer

    def patch(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response({
            'success': True,
            'message': 'Password reset success'
        },
                        status=status.HTTP_200_OK)


class LogoutAPIView(generics.GenericAPIView):
    permission_classes = (permissions.IsAuthenticated, )
    serializer_class = LogoutSerializer

    def post(self, request):

        request.user.auth_token.delete()
        logout(request)
        return Response(status=status.HTTP_200_OK)
