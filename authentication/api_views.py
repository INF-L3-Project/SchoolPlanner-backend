from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import viewsets, generics, status, permissions
from rest_framework.mixins import CreateModelMixin, UpdateModelMixin, DestroyModelMixin
from authentication.serializers import InstitutionSerializer, LoginSerializer, LoginUserSerializer, LogoutSerializer
from authentication.models import Institution
from django.contrib.auth import authenticate, login, logout
from rest_framework.exceptions import AuthenticationFailed


class InstitutionViewSet(CreateModelMixin, UpdateModelMixin, DestroyModelMixin,
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


class LogoutAPIView(generics.GenericAPIView):
    permission_classes = (permissions.IsAuthenticated, )
    serializer_class = LogoutSerializer

    def post(self, request):

        request.user.auth_token.delete()
        logout(request)
        return Response(status=status.HTTP_200_OK)
