from django.contrib import admin
from .models import Account, Withdraw

class TransactionalAdmin(admin.ModelAdmin):
    list_display = (
        "sender", "receiver", "account_number", "amount", "reference",
        "status"
    )
admin.site.register(Withdraw)

class AccountAdmin(admin.ModelAdmin):
    list_display = (
        "user", "user_qrcode", "account_number", "account_id", "first_name",
        "last_name"
    )
admin.site.register(Account)