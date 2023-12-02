from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from .serializers import UserRegistrationSerializer, LoginSerializer, NextOfKinSerializer, NationalIdentificationNumberSerializer, BankVerificationNumberSerializer, BasicInformationSerializer
from .models import User
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework import generics, permissions
from rest_framework.authtoken.models import Token


def home(request):
    return render(request, 'Home.html')
@api_view(['GET'])
def get_all(request):
    user = User.objects.all()
    serializer = UserRegistrationSerializer(user, many=True)
    return Response(serializer.data)

class RegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = (permissions.AllowAny,)

class LoginSerializerView(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request':request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key, 'user_id': user.pk})
        
@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def validate_bvn_number(request):
    if request.method == 'POST':
        serializer = BankVerificationNumberSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def validate_nin_number(request):
    if request.method == 'POST':
        serializer = NationalIdentificationNumberSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def create_basic_information(request):
    if request.method == 'POST':
        serializer = BasicInformationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def create_next_of_king(request):
    if request.method == 'POST':
        serializer = NextOfKinSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)