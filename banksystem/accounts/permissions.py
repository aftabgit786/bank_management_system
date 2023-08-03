from rest_framework.permissions import BasePermission


class MyCustomPermission(BasePermission):
    message = "Only Aftab can enter"

    def has_permission(self, request, view):
        return request.user.first_name == 'aftab'
