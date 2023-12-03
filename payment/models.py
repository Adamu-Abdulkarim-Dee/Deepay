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
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='sender_account')
    receiver = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='receiver_account')
    amount = models.DecimalField(max_digits=50, decimal_places=6)
    account_number = models.BigIntegerField()
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    status = models.CharField(max_length=50, choices=STATUS)
    pin = models.CharField(max_length=5)
    reference_number = models.CharField(max_length=50, default=reference_number, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.sender)