# Django Imports
from django.contrib.auth.models import User
# Rest Imports
from rest_framework import serializers
# Python Imports
from logging import getLogger

# Local Imports

# Loggers
log = getLogger(__name__)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'is_superuser', 'username', 'is_active')

    def create(self, validated_data):
        return User.objects.create(**validated_data)
