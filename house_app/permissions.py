from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.role == 'admin'
        )

class IsSeller(BasePermission):
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.role == 'seller'
        )

class IsBuyer(BasePermission):
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.role == 'buyer'
        )

class CanCreateProperty(BasePermission):
    def has_permission(self, request, view):
        return (
            request.method == 'POST'
            and request.user.is_authenticated
            and request.user.role == 'seller'
        )

class IsOwnerOfProperty(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.seller == request.user

class ReadOnlyOrSeller(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return (
            request.user.is_authenticated
            and request.user.role == 'seller'
        )

class CanCreateReview(BasePermission):
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.role == 'buyer'
        )
