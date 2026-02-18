from  .models import CustomUser
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from .serializers import RegisterSerializer, LoginSerializer, CustomUserSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import action
from rest_framework import viewsets
from django.shortcuts import get_object_or_404

class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAuthenticated]
    
class RegisterView(CreateAPIView):
    """API endpoint for new user registration. Auto-generates token."""
    serializer_class = RegisterSerializer  # Uses RegisterSerializer above
    permission_classes = [AllowAny]  # Allow anyone to register (override global auth)

class LoginView(CreateAPIView):
    """API endpoint for user login. Returns token and user info."""
    serializer_class = LoginSerializer
    permission_classes = [AllowAny]  # Allow anyone to attempt login (override global auth)
    
    def post(self, request):
        # Validate input data
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data  # Authenticated user
        
        # Get or create token for this user
        token, _ = Token.objects.get_or_create(user=user)
        # Return token and basic user data (customize as needed)
        return Response({
            'token': token.key, 
            'user': {'id': user.id, 'username': user.username}
        }, status=status.HTTP_200_OK)

class RetrieveTokenView(CreateAPIView):
   
    permission_classes = [IsAuthenticated]

    """Retrieve current user's token (requires prior authentication)."""
    def post(self, request):
        user = request.user  # From TokenAuthentication
        if user.is_authenticated:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})
        return Response(status=status.HTTP_401_UNAUTHORIZED)
       
class FollowUserView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        target = get_object_or_404(CustomUser, id=user_id)
        request.user.following.add(target)
        return Response({"status": f"You are now following {target.username}"})


class UnfollowUserView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        target = get_object_or_404(CustomUser, id=user_id)
        request.user.following.remove(target)
        return Response({"status": f"You have unfollowed {target.username}"})