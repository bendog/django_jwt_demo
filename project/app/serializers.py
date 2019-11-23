
from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Profile
        

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(many=False, required=False)
    groups = GroupSerializer(many=True, required=False, read_only=True)
    class Meta:
        model = User
        fields = ['id', 'url', 'username', 'email', 'groups', 'profile']
