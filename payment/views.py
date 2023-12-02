from django.shortcuts import render
from .models import Account, Withdraw
from .serializers import WithdrawSerializer, AccountSerializer, CommissionToAccountTransactionSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions

@api_view(['POST'])
def create_withdraw(request):
    if request.method == 'POST':
        serializer = WithdrawSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def create_commission_to_account_transaction(request):
    if request.method == 'POST':
        serializer = CommissionToAccountTransactionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def account(request):
    if request.method == 'GET':
        accounts = Account.objects.filter(user=request.user.id)
        serializer = AccountSerializer(accounts, many=True)
        return Response(serializer.data)

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_credited_transaction(request):
    if request.method == 'GET':
        credited_transactions = Withdraw.objects.filter(credited=request.user.id)
        serializer = WithdrawSerializer(credited_transactions, many=True)
        return Response(serializer.data)

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_debited_transaction(request):
    if request.method == 'GET':
        debited_transactions = Withdraw.objects.filter(debited=request.user.id)
        serializer = WithdrawSerializer(debited_transactions, many=True)
        return Response(serializer.data)