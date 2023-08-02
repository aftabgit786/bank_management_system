from rest_framework import generics
from rest_framework.permissions import IsAdminUser

from .serializer import BankSerializer
from .models import Bank


class GetBanksAPIView(generics.ListAPIView):
    serializer_class = BankSerializer
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        user = self.request.user
        user_banks = Bank.objects.filter(bank_accounts__user=user)

        return user_banks
