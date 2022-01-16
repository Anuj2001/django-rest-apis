from rest_framework.permissions import BasePermission

class CustomPermissions(BasePermission):
    def has_permission(self, request, view):
        if request.method=='GET' or request.method =='PUT':
            return True
        return False