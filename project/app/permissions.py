from rest_framework import permissions


class IsAdminOrSelf(permissions.BasePermission):
    """
    Object-level permission to only allow modifications to a User object
    if the request.user is an administrator or you are modifying your own
    user object.
    """

    def has_object_permission(self, request, view, obj):
        return request.user.is_staff or request.user == obj
