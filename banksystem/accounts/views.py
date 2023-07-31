from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from .utils import get_user_bank_accounts
from .serializer import AccountSerializer


class GetBankAccount(APIView):

    def get(self, *args, **kwargs):
        bank_id = self.kwargs.get('bank_id')
        accounts = get_user_bank_accounts(self.request, bank_id=bank_id)
        serializer = AccountSerializer(accounts, many=True)
        return Response({'accounts': serializer.data})


@api_view(['GET'])
def get_bank_accounts(request, bank_id):
    user_account_context = get_user_bank_accounts(request, bank_id)
    serializer = AccountSerializer(user_account_context, many=True)

    return Response({'accounts': serializer.data})
