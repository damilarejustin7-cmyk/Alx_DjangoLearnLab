# DRF serializers for data validation/serialization
from rest_framework import serializers
# Built-in auth for password checking during login
from django.contrib.auth import authenticate
# Import our custom user model
from .models import CustomUser
# Token model for generating/retrieving auth tokens
from rest_framework.authtoken.models import Token

class RegisterSerializer(serializers.ModelSerializer):
    """
    Serializer for user registration.
    Hashes password securely and auto-creates token.
    """
    # Hide password from response but require it for input
    password = serializers.CharField(write_only=True)
    
    class Meta:
        model = CustomUser
        # Fields to expose; add more as needed (e.g., first_name)
        fields = ('username', 'email', 'password', 'bio', 'profile_picture')
    
    def create(self, validated_data):
        # Create user with hashed password (create_user handles hashing)
        user = CustomUser.objects.create_user(**validated_data)
        # Generate and save token for immediate use
        Token.objects.create(user=user)
        return user

class LoginSerializer(serializers.Serializer):
    """
    Serializer for login credentials validation.
    Returns authenticated user or raises error.
    """
    username = serializers.CharField()
    password = serializers.CharField()
    
    def validate(self, data):
        # Authenticate using Django's built-in function
        user = authenticate(**data)
        if user and user.is_active:  # Check if account is active
            return user
        raise serializers.ValidationError("Invalid credentials.")
