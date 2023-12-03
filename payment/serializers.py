from rest_framework import serializers
from .models import Withdraw, Account, ExternalTransaction
from rest_framework.fields import CurrentUserDefault

class ExternalTransactioSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExternalTransaction
        fields = "__all__"

        def validated_data(self, validated_data):
            pass

class WithdrawSerializer(serializers.ModelSerializer):
    class Meta:
        model = Withdraw
        fields = '__all__'

        def validate(self, validated_data):
            sender = self.context['request'].user
            amount = self.validated_data['amount']
            account_number = self.validated_data['account_number']
            pin = self.validated_data['pin']

            sender_account = Account.objects.get(user=sender)
            receiver_account = Account.objects.get(account_number=account_number)

            if sender_account.pin != pin:
                raise serializers.ValidationError({"detail": "Incorrect Pin 03"})

            if sender_account.account_number == account_number:
                raise serializers.ValidationError({"detail": "Transaction Not Allowed 04"})

            if sender_account.account_balance >= amount:
                sender_account.account_balance -= amount
                sender_account.save()

                receiver_account.account_balance += amount
                receiver_account.save()
                
                Withdraw.objects.create(
                    sender=sender_account.user, receiver=receiver_account.user, amount=amount, pin=pin,
                    first_name=receiver_account.first_name, last_name=receiver_account.last_name,
                    status='SUCCESS(00)', account_number=account_number
                )
            else:
                raise serializers.ValidationError({"detail": "INSUFFICIENT_FUNDS_05"})

class AccountSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())
    class Meta:
        model = Account
        fields = '__all__'
