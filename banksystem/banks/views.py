from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from .utils import get_user_banks
from .serializer import BankSerializer


class GetBanks(APIView):
    def get(self, *args, **kwargs):
        user_banks = get_user_banks(self.request)
        serializer = BankSerializer(user_banks, many=True)

        return Response({'banks': serializer.data})


@api_view(['GET'])
def get_banks(request):
    user_banks = get_user_banks(request)
    serializer = BankSerializer(user_banks, many=True)

    return Response({'banks': serializer.data})
