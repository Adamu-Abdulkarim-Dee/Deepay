from rest_framework import serializers
from .models import Transaction, Account
from rest_framework.fields import CurrentUserDefault
import cv2

class AccountSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())
    class Meta:
        model = Account
        fields = '__all__'

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'

        def validate(self, validated_data):
            sender = CurrentUserDefault
            finger_print = self.validated_data['finger_print']
            amount = self.validated_data['amount']
            account_number = self.validated_data['account_number']
            first_name = self.validated_data['first_name']
            last_name = self.validated_data['last_name']
            status = self.validated_data['status']
            pin = self.validated_data['pin']

            credited_account = Account.objects.get(user=sender)

            debited_account = Account.objects.get(account_number=account_number)

            #   Accessing debited fingerprint
            debited_finger_print = debited_account.finger_print

            if debited_account.pin != pin:
                raise serializers.ValidationError("Incorrect Pin")

            if debited_account.account_number == credited_account.account_number:
                raise serializers.ValidationError("Invalid Account Number 00")

            if debited_account.account_balance >= amount:
                debited_account.account_balance -= amount
                debited_account.save()

                credited_account.account_balance += amount
                credited_account.save()
                
                Transaction.objects.create(
                    sender=credited_account.user, receiver=debited_account, amount=amount, pin=pin,
                    first_name=debited_account.first_name, last_name=debited_account.last_name,
                    status='Success', finger_print=debited_finger_print, account_number=account_number
                )
            else:
                raise serializers.ValidationError("INSUFFICIENT FUNDS 01")
                return validated_data

class ChoiceField(serializers.Field):
    def __init__(self, choices, **kwargs):
        self._choices = choices
        super(ChoiceField, self).__init__(**kwargs)

    def to_representation(self, obj):
        return self._choices[obj]

    def to_internal_value(self, data):
        return getattr(self._choices, data)
