from rest_framework import permissions

class IsManager(permissions.BasePermission):
    """
    Custom permission to only allow managers to access.
    """
    def has_permission(self, request, view):
        return request.user.groups.filter(name='Manager').exists()

class IsDeliveryCrewOrManager(permissions.BasePermission):
    """
    Custom permission to only allow delivery crew or managers to access.
    """
    def has_permission(self, request, view):
        return (request.user.groups.filter(name='Delivery crew').exists() or 
                request.user.groups.filter(name='Manager').exists())

class IsManagerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow managers to edit, but allow read-only access to everyone.
    """
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.groups.filter(name='Manager').exists()

class IsOwnerOrManager(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object or managers to access it.
    """
    def has_object_permission(self, request, view, obj):
        # Read permissions for anyone
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # Write permissions only to the owner or managers
        return obj.user == request.user or request.user.groups.filter(name='Manager').exists()

class IsCustomer(permissions.BasePermission):
    """
    Permission to allow access only to customers (users not in Manager or Delivery crew groups).
    """
    def has_permission(self, request, view):
        if request.user and request.user.is_authenticated:
            return not (request.user.groups.filter(name='Manager').exists() or 
                       request.user.groups.filter(name='Delivery crew').exists())
        return False

class IsDeliveryCrew(permissions.BasePermission):
    """
    Permission to allow access only to delivery crew members.
    """
    def has_permission(self, request, view):
        if request.user and request.user.is_authenticated:
            return request.user.groups.filter(name='Delivery crew').exists()
        return False
