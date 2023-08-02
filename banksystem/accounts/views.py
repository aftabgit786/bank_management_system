from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied

from .models import Account
from .serializer import AccountSerializer


class GetBankAllAccountAPIView(generics.ListAPIView):
    serializer_class = AccountSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user_accounts = Account.objects.filter(user=self.request.user)

        return user_accounts


class GetBankAccountViaIdsAPIView(generics.RetrieveAPIView):
    serializer_class = AccountSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        try:
            accounts = Account.objects.get(pk=self.kwargs['pk'], user=self.request.user)

            return accounts

        except Account.DoesNotExist:
            raise PermissionDenied("You do not have permission to access this account.")
