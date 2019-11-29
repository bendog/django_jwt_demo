from django.contrib.auth.models import User, Group
from django.db import transaction
from rest_framework import serializers

from .models import Profile
from app.helpers import send_password_reset_email


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        exclude = ['user']


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class UserSerializer(serializers.ModelSerializer):
    profile = UserProfileSerializer(many=False, required=False)
    groups = GroupSerializer(many=True, required=False, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'url', 'username', 'email', 'first_name', 'last_name', 'groups', 'profile']

    @transaction.atomic
    def create(self, validated_data):
        # remove the profile data
        profile_data = validated_data.pop('profile')
        # create user from validated data
        user = User(**validated_data)
        # set user password to blank
        user.set_unusable_password()
        # save the user
        user.save()
        # update the user profile
        Profile.objects.filter(user=user).update(**profile_data)

        # send user password setup email
        send_password_reset_email(user)
        return user

    def update(self, instance, validated_data):
        # remove the profile data
        profile_data = validated_data.pop('profile')
        # run the normal update process
        super().update(instance, validated_data)
        # handle extra profile information
        if profile_data:
            Profile.objects.filter(user=instance).update(**profile_data)
        return instance


class PasswordSerializer(serializers.Serializer):
    """
    Serializer for password change endpoint.
    """
    new_password = serializers.CharField(required=True)
