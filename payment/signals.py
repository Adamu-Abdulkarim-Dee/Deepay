from django.conf import settings
from .models import Account, Withdraw, CommissionAccount
from django.db.models.signals import post_save
from django.dispatch import receiver
import random
import  string

def generate_account_number():
    logic = '88' + ''.join(random.choices(string.digits, k=8))
    return logic

def generate_account_id():
    logic = '22' + ''.join(random.choices(string.digits, k=9)) 
    return logic

def generate_account_id_commission():
    logic = '20' + ''.join(random.choices(string.digits, k=9)) 
    return logic

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_account(instance, created, sender, **kwargs):
    if created:
        account_number = generate_account_number()
        account_id = generate_account_id()
        account_id_c = generate_account_id_commission()
        first_name = instance.first_name
        last_name = instance.last_name
        Account.objects.create(
            user=instance, account_number=account_number, account_id=account_id,
            first_name=first_name, last_name=last_name,
            account_status='ACTIVE', account_balance=0, pin=0000
        )
        CommissionAccount.objects.create(
            user=instance, account_id=account_id_c,
            account_balance=0, account_status='ACTIVE'
        ) 
