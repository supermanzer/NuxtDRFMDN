"""
    api/serializers.py

    Define general purpose custom serializers
"""

from rest_framework import serializers
from myauth.models import User


class UserSerializer(serializers.ModelSerializer):
    group = serializers.SerializerMethodField()

    def get_group(self, object):
        return object.groups.first().name

    class Meta:
        model = User
        fields = ('last_login', 'first_name', 'last_name',
                  'email', 'is_staff', 'group')
