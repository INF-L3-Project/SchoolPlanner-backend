from rest_framework.authtoken.models import Token
from rest_framework.serializers import ModelSerializer, ReadOnlyField, ValidationError
from authentication.models import Institution
from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib import auth
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

    def validate(self, attrs):
        email = attrs.get('email', '')
        username = attrs.get('username', '')

        if not User.objects.filter(email=email).first():
            raise ValidationError('an account with this email already exits')
        return attrs

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