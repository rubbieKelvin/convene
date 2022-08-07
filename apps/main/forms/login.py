from rest_framework import serializers
from apps.main.models.user import User
from rest_framework.authtoken.models import Token

from apps.main import queries

def password_validator(value):
    pass

class LoginForm(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(validators=[password_validator])

    def validate(self, attrs):
        user: User = queries.usersAll().filter(email=attrs['email']).first()
        if not user:
            raise serializers.ValidationError("user not found")
        if not user.check_password(attrs['password']):
            raise serializers.ValidationError("incorrect password")

        # create token
        token: Token = Token.objects.filter(user=user).first()
        if not token:
            token = Token.objects.create(user=user)

        return {
            'user': user,
            'token': token,
        }