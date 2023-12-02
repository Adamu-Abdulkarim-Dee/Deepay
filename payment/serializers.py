from rest_framework import serializers
from .models import Withdraw, Account, CommissionToAccountTransaction, CommissionAccount
from rest_framework.fields import CurrentUserDefault
import cv2


class CommissionToAccountTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommissionToAccountTransaction
        fields = "__all__"

        def validate(self, validated_data):
            sender = self.context['request'].user
            account_id = self.validated_data['account_id']
            amount = self.validated_data['amount']
            pin = self.validated_data['pin']

            sender_account = CommissionAccount.objects.get(user=sender)
            receiver_account = Account.objects.get(account_id=account_id)

            if sender_account.user != receiver_account.user:
                raise serializer.ValidationError({"detail": "Transaction Not Allowed"})

            if sender_account.pin != pin:
                raise serializer.ValidationError({"detail": "Incorrect Pin"})

            if sender_account.account_balance >= amount:
                sender_account.account_balance -= amount
                sender_account.save()

                receiver_account.account_balance += amount
                receiver_account.save()
                CommissionToAccountTransaction.objects.create(
                    sender=sender_account.user, receiver=receiver_account,
                    account_id=account_id, amount=amount, pin=pin
                )
            else:
                raise serializer.ValidationError({"detail": "INSUFFICIENT_FUNDS_05"})

class WithdrawSerializer(serializers.ModelSerializer):
    class Meta:
        model = Withdraw
        fields = '__all__'

        def validate(self, validated_data):
            credited = self.context['request'].user
            finger_print = self.validated_data['finger_print']
            amount = self.validated_data['amount']
            account_number = self.validated_data['account_number']
            first_name = self.validated_data['first_name']
            last_name = self.validated_data['last_name']
            status = self.validated_data['status']
            pin = self.validated_data['pin']

            credited_account = Account.objects.get(user=sender)
            debited_account = Account.objects.get(account_number=account_number)

            if debited_account.pin != pin:
                raise serializers.ValidationError({"detail": "Incorrect Pin 03"})

            if debited_account.account_number == credited_account.account_number:
                raise serializers.ValidationError({"detail": "Invalid Account Number 04"})

            if debited_account.account_balance >= amount:
                debited_account.account_balance -= amount
                debited_account.save()

                credited_account.account_balance += amount
                credited_account.save()
                
                Withdraw.objects.create(
                    credited=credited_account.user, receiver=debited_account.user, amount=amount, pin=pin,
                    first_name=debited_account.first_name, last_name=debited_account.last_name,
                    status='SUCCESS(00)', finger_print=debited_finger_print, account_number=account_number
                )
            else:
                raise serializers.ValidationError({"detail": "INSUFFICIENT_FUNDS_05"})
            return validated_data

class AccountSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())
    class Meta:
        model = Account
        fields = '__all__'
