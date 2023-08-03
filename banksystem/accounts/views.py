from rest_framework import generics
from rest_framework.generics import get_object_or_404
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle

from .models import Account
from .pagination import AdminResultsPagination
from .serializer import AccountSerializer
from .permissions import MyCustomPermission


class BankListAPIView(generics.ListAPIView):
    serializer_class = AccountSerializer
    permission_classes = [MyCustomPermission]
    throttle_classes = [UserRateThrottle, AnonRateThrottle]

    def get_queryset(self):
        return Account.objects.filter(user=self.request.user)


class BankDetailAPIView(generics.RetrieveAPIView):
    serializer_class = AccountSerializer
    permission_classes = [MyCustomPermission]
    throttle_classes = [UserRateThrottle, AnonRateThrottle]

    def get_object(self):
        return get_object_or_404(Account, pk=self.kwargs['pk'], user=self.request.user)


class AdminBankListAPIView(generics.ListAPIView):
    serializer_class = AccountSerializer
    pagination_class = AdminResultsPagination
    throttle_classes = [UserRateThrottle, AnonRateThrottle]

    def get_queryset(self):
        queryset = Account.objects.all()
        user_id = self.request.query_params.get('user', None)
        if user_id:
            queryset = queryset.filter(user_id=user_id)
        return queryset
