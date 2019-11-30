from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.contrib.auth.models import User, Group
from rest_framework import viewsets, generics, status
from rest_framework.decorators import action

from .permissions import IsAdminOrSelf
from .serializers import UserSerializer, GroupSerializer, ProfileSerializer, PasswordSerializer
from .models import Profile
from .helpers import send_password_reset_email


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = User.objects.none()
    serializer_class = UserSerializer

    # permission_classes = (IsAuthenticated, IsAdminUser)

    def get_queryset(self):
        # if the user is admin, return all the users
        if self.request.user.is_superuser:
            return User.objects.all().order_by("-date_joined")
        # if the user is logged in, return only the active user
        if self.request.user:
            return User.objects.filter(pk=self.request.user.pk)
        # if there is no user, return no results
        return User.objects.none()

    @action(methods=["post"], detail=True, permission_classes=[IsAdminOrSelf])
    def set_password(self, request, pk=None):
        """ set the user password """
        serializer = PasswordSerializer(data=request.data)
        user = self.get_object()

        if serializer.is_valid():
            user.set_password(serializer.data.get("new_password"))
            user.save()
            return Response({"status": "password set"}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(methods=["get"], detail=True, permission_classes=[IsAdminOrSelf])
    def reset_password(self, request, pk=None):
        """ set the user password """
        user = self.get_object()
        send_password_reset_email(user)

        return Response({"status": "password reset"}, status=status.HTTP_200_OK)


class ProfileViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (IsAuthenticated,)


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """

    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class HelloView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {"message": "Hello, World!"}
        return Response(content)
