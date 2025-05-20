
from rest_framework import serializers
from .models import UserAccount

from djoser.serializers import UserCreateSerializer
from rest_framework import serializers

class UserAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields = ['email', 'first_name', 'last_name', 'balance']


class CustomUserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = UserAccount
        fields = ['id', 'email', 'password', 're_password', 'first_name', 'last_name']
