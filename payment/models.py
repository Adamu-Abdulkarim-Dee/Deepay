from django.db import models
from django.conf import settings
import random
import string
from .choices import *

class Account(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    account_number = models.BigIntegerField(unique=True)
    account_balance = models.DecimalField(max_digits=12, decimal_places=6, default=0)
    account_id = models.CharField(max_length=15, unique=True)
    finger_print = models.ImageField()
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    account_status = models.CharField(max_length=50, choices=ACCOUNT_STATUS)
    pin = models.CharField(max_length=5)
    
    def __str__(self):
        return str(self.user.first_name)

def reference_number():
    start = 'id' + ''.join(random.choices(string.digits, k=20))
    return start

class Transaction(models.Model):
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    receiver = models.ForeignKey(Account, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=12, decimal_places=6)
    account_number = models.BigIntegerField()
    finger_print = models.ImageField()
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    status = models.CharField(max_length=50, choices=STATUS)
    reference = models.CharField(max_length=30, default=reference_number, unique=True)
    pin = models.CharField(max_length=5)

    def __str__(self):
        return str(self.sender)

class Complaint(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    message = models.TextField()
    select = models.CharField(max_length=225, choices=TYPE_OF_COMPLAINT)
    language = models.CharField(max_length=255, choices=LANGUAGE)