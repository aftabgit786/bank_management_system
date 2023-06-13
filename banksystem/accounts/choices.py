from django.db import models
from django.utils.translation import gettext_lazy as _


class Types(models.TextChoices):
    CURRENT = "CA", _("Current")
    SAVINGS = "SA", _("Savings")
    LOAN = "L", _("Loan")
    FIXED_DEPOSIT = "FD", _("Fixed Deposit")
    OTHER = "O", _("Other")
