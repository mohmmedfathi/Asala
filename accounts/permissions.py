from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsAdminOrOwner(BasePermission):


    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return request.user and request.user.is_authenticated
        return request.user and request.user.is_authenticated and request.user.is_staff

    def has_object_permission(self, request, view, obj):
        if request.user.is_staff:
            return True
        return obj == request.user

class IsAdminOrProductBuyer(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.is_staff or request.user in obj.buyers.all()