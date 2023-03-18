from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """ Only allow owner to edit """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user == obj.author.user
