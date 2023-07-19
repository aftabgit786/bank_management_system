from .models import Account


def get_user_bank_accounts(request, bank_id):
    user = request.user
    user_account_context = Account.objects.filter(user=user, bank_id=bank_id)

    return user_account_context
