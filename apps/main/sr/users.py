from apps.main.models.user import User
from rest_framework.serializers import ModelSerializer

class UserSr(ModelSerializer):
    class Meta:
        model = User
        exclude = ['password', 'user_permissions']
