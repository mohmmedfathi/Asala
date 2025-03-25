from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsAdminOrOwner(BasePermission):
    """
    - All users can view (read-only access).
    - Only admins can create, update, or delete any object.
    - Normal users can only see their own objects.
    """

    def has_permission(self, request, view):
        # Allow all users to list or retrieve objects (safe methods)
        if request.method in SAFE_METHODS:
            return request.user and request.user.is_authenticated
        # Allow non-safe methods only for admin users
        return request.user and request.user.is_authenticated and request.user.is_staff

    def has_object_permission(self, request, view, obj):
        # Admins can do everything
        if request.user.is_staff:
            return True
        # Normal users can only access objects they own
        return obj.owner == request.user
