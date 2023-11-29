from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager
from .choices import STATE, RELATIONSHIP

class User(AbstractUser):
    username = models.CharField(max_length=15, unique=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15)
    is_developer = models.BooleanField(default=False)
    is_organization = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    objects = CustomUserManager()

    def __str__(self):
        return str(self.username)

class BasicInformation(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    state = models.CharField(max_length=255, choices=STATE)
    local_government = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)
    date_of_birth = models.DateField()
    utility_bill = models.ImageField()

    def __str__(self):
        return str(self.user)

class NationalIdentificationNumber(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nin_number = models.BigIntegerField()
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

class BankVerificationNumber(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    bvn_number = models.BigIntegerField()
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()

    def __str__(self):
        return str(self.user)

class NextOfKin(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nin_number = models.BigIntegerField()
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    phone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=50)
    profile_photo = models.ImageField(null=True, blank=True)
    relationship = models.CharField(max_length=50, choices=RELATIONSHIP)
    def __str__(self):
        return self.user

    def __str__(self):
        return str(self.user)