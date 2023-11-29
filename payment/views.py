from django.shortcuts import render
from .models import Account, Transaction
from .serializers import TransactionSerializer, AccountSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from decimal import Decimal

def transfer(request):
    if request.method == 'POST':
        amount = Decimal(request.POST['amount'])
        pin = request.POST['pin']
        account_number = request.POST['account_number']
        finger_print = request.FILES['finger_print']

        receiver_account = Account.objects.get(account_number=account_number)
        sender_account = Account.objects.get(user=request.user)

        if receiver_account.account_balance >= amount:
            receiver_account.account_balance -= amount
            receiver_account.save()

            sender_account.account_balance += amount
            sender_account.save()
            create_transaction = Transaction.objects.create(
                sender=sender_account.user, receiver=receiver_account, amount=amount, last_name=receiver_account.last_name,
                first_name=receiver_account.first_name, pin=pin, status='Success', finger_print=receiver_account.finger_print

            )
    return render(request, 'home.html')

class TransactionalView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self, request, format=None):
        serializer = TransactionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AccountView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    def get_object(self, pk):
        try:
            return Account.objects.get(pk=pk)
        except Account.DoesNotExist:
            raise Http404

    def put(self, request, pk, format=None):
        account = self.get_object(pk)
        serializer = AccountSerializer(account, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
