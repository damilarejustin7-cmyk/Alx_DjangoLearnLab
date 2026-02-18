# DRF imports for API views and responses
from  .models import CustomUser # Our custom user model
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
# Token model for login/retrieval
from rest_framework.authtoken.models import Token
# Our serializers
from .serializers import RegisterSerializer, LoginSerializer, CustomUserSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import action
from rest_framework import viewsets

class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
    def follow(self, request, pk=None):
        user_to_follow = self.get_object()
        request.user.following.add(user_to_follow)
        return Response({"message": "Followed successfully."})

    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
    def unfollow(self, request, pk=None):
        user_to_unfollow = self.get_object()
        request.user.following.remove(user_to_unfollow)
        return Response({"message": "Unfollowed successfully."})
    
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
       