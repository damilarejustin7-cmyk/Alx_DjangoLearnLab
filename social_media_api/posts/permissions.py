# posts/permissions.py
from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission: Read for all, edit/delete only by owner.
    """
    def has_object_permission(self, request, view, obj):
        # Safe methods (GET, HEAD, OPTIONS) allowed for everyone
        if request.method in permissions.SAFE_METHODS:
            return True
        # Write methods (PUT, PATCH, DELETE) only for owner
        return obj.author == request.user
