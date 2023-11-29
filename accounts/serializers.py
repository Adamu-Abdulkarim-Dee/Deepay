from rest_framework import serializers
from .models import User, NextOfKin, NationalIdentificationNumber, BankVerificationNumber, BasicInformation
from django.contrib.auth import authenticate


class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'username', 'password', 'first_name', 'last_name', 'phone_number']

        def create(self, validated_data):
            user = User.objects.create_user(
                username=validated_data['username'],
                email=validated_data['email'],
                password=validated_data['password'],
                first_name=validated_data['first_name'],
                last_name=validated_data['last_name'],
                phone_number=validated_data['phone_number']
            )
            return user

class LoginSerializer(serializers.Serializer):
    
    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    data['user'] = user
                else:
                    raise serializers.ValidationError('User account is disable.')
            else:
                raise serializers.ValidationError('Unable to log in with provided credentials.')
        else:
            raise serializers.ValidationError('Must provide both email and password')
        return data

class BankVerificationNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankVerificationNumber
        fields = '__all__'

class BasicInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = BasicInformation
        fields = '__all__'

class NationalIdentificationNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = NationalIdentificationNumber
        fields = '__all__'

class NextOfKinSerializer(serializers.ModelSerializer):
    class Meta:
        model = NextOfKin
        fields = '__all__'