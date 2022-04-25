import email
from rest_framework.authtoken.models import Token
from rest_framework.serializers import ModelSerializer, ReadOnlyField, ValidationError
from authentication.models import Institution
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.exceptions import AuthenticationFailed
#from rest_framework_simplejwt.tokens import RefreshToken, TokenError
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import smart_str, force_str, smart_bytes, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode


class UserSerializer(ModelSerializer):

    username = ReadOnlyField()

    class Meta:
        model = User
        fields = ('id', 'last_name', 'email', 'username', 'password')


class InstitutionSerializer(ModelSerializer):

    user = UserSerializer()

    class Meta:
        model = Institution
        fields = ('id', 'user', 'name', 'logo', 'description')

    def validate(self, data):
        """
        Check if there an user with the same email.
        """
        new_user = data['user']
        new_username = new_user['email']
        if Institution.objects.filter(
                user__username=new_username).exists():
            raise serializers.ValidationError(
                "This email has already registered")
        return data

    def create(self, validated_data):

        user_data = validated_data.pop('user')
        last_name = user_data['last_name']
        username = user_data['email']
        email = user_data['email']
        password = user_data['password']
        user = User.objects.create_user(username=username,
                                        last_name=last_name,
                                        email=email,
                                        password=password)

        return Institution.objects.create(
            user=user,
            name=validated_data['name'],
            logo=validated_data['logo'],
            description=validated_data['description'])


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=255, min_length=3)
    password = serializers.CharField(max_length=68, min_length=6)


class LogoutSerializer(serializers.Serializer):
    pass


class LoginUserSerializer(ModelSerializer):

    token = serializers.SerializerMethodField()

    def get_token(self, instance: User):
        return Token.objects.get(user=instance).key

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'last_name', 'token')


class ResetPasswordEmailRequestSerializer(serializers.Serializer):
    email = serializers.EmailField(min_length=2)

    redirect_url = serializers.CharField(max_length=500, required=False)

    class Meta:
        fields = ['email']


class SetNewPasswordSerializer(serializers.Serializer):
    password = serializers.CharField(min_length=6,
                                     max_length=68,
                                     write_only=True)
    token = serializers.CharField(min_length=1, write_only=True)
    uidb64 = serializers.CharField(min_length=1, write_only=True)

    class Meta:
        fields = ['password', 'token', 'uidb64']

    def validate(self, attrs):
        try:
            password = attrs.get('password')
            token = attrs.get('token')
            uidb64 = attrs.get('uidb64')

            id = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(id=id)
            if not PasswordResetTokenGenerator().check_token(user, token):
                raise AuthenticationFailed('The reset link is invalid', 401)

            user.set_password(password)
            user.save()

            return super().validate(attrs)
        except Exception as e:
            raise AuthenticationFailed('The reset link is invalid', 401)
