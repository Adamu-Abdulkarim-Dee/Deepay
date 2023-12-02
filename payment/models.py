from django.db import models
from django.conf import settings
import random
import string
from .choices import *

class CommissionAccount(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    account_balance = models.DecimalField(max_digits=50, decimal_places=6)
    account_id = models.BigIntegerField()
    account_status = models.CharField(max_length=50, choices=ACCOUNT_STATUS)
    def __str__(self):
        return str(self.user)

class Account(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    account_number = models.BigIntegerField(unique=True)
    account_balance = models.DecimalField(max_digits=50, decimal_places=6)
    tid_number = models.CharField(max_length=12)
    account_id = models.BigIntegerField(max_length=15, unique=True)
    finger_print = models.ImageField(default='staticfiles/demo.png')
    first_name = models.CharField(max_length=70)
    last_name = models.CharField(max_length=70)
    account_status = models.CharField(max_length=50, choices=ACCOUNT_STATUS)
    pin = models.CharField(max_length=5)
    
    def __str__(self):
        return str(self.user)

def reference_number():
    # Change 884 after each month
    start = '884' + ''.join(random.choices(string.digits, k=40))
    return start

class Withdraw(models.Model):
    credited = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    debited = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='debited_user')
    amount = models.DecimalField(max_digits=50, decimal_places=6)
    account_number = models.BigIntegerField()
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    status = models.CharField(max_length=50, choices=STATUS)
    pin = models.CharField(max_length=5)
    reference_number = models.CharField(max_length=50, default=reference_number, unique=True)
    tid_number = models.CharField(max_length=12)
    fee_to_customer = models.IntegerField()
    agent_account_id = models.BigIntegerField()
    agent_commission = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.credited)

class CommissionToAccountTransaction(models.Model):
    account_id = models.BigIntegerField()
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    receiver = models.ForeignKey(Account, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=50, decimal_places=6)
    pin = models.CharField(max_length=5)
    reference_number = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)