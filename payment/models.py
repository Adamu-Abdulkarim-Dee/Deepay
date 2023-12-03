from django.db import models
from django.conf import settings
import random
import string
from .choices import *

class Account(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    account_number = models.BigIntegerField(unique=True)
    account_balance = models.DecimalField(max_digits=50, decimal_places=6)
    qr_code = models.ImageField()
    account_name = models.CharField(max_length=150)
    account_status = models.CharField(max_length=50, choices=ACCOUNT_STATUS)
    pin = models.CharField(max_length=5)
    
    def __str__(self):
        return str(self.user)

def reference_number():
    # Change 884 after each month
    start = '884' + ''.join(random.choices(string.digits, k=40))
    return start

class Withdraw(models.Model):
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='sender_account')
    receiver = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='receiver_account')
    amount = models.DecimalField(max_digits=50, decimal_places=6)
    account_number = models.BigIntegerField()
    account_name = models.CharField(max_length=150)
    status = models.CharField(max_length=50)
    pin = models.CharField(max_length=5)
    reference_number = models.CharField(max_length=50, default=reference_number, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.sender)

class ExternalTransaction(models.Model):
    receiver = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    account_number = models.BigIntegerField()
    sender_account_number = models.BigAutoField()
    sender_full_name = models.CharField(max_length=150)
    sender_bank_name = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=50, decimal_places=6)
    recipient_account_name = models.CharField(max_length=150)
    status = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)