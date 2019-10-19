__author__ = "Sanjeev Kumar"
__email__ = "sanju.sci9@gmail.com"
__copyright__ = "Copyright 2019."

from django.contrib.auth.models import User
from rest_framework import serializers
from api.user.model import UserProfile


class UserProfileSerializer(serializers.ModelSerializer):
    """Serializer for user profile."""

    class Meta:
        model = UserProfile
        fields = '__all__'
        read_only_fields = ('id', 'created_timestamp')


class UserSerializer(serializers.ModelSerializer):
    """Serializer for users."""

    class Meta:
        model = User
        fields = (
                'id',
                'first_name',
                'last_name',
                'username',
                'email',
                'is_active'
                )
        read_only_fields = ('id', )

