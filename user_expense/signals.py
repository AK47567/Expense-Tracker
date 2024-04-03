from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from .models import Expenses, Account

@receiver(m2m_changed, sender=Expenses.account.through)
def update_account_balance(sender, instance, action, **kwargs):
    if action == "post_add":
        for account in instance.account.all():
            account.balance -= instance.amount
            account.save()
