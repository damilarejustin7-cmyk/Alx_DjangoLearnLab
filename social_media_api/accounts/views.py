# DRF imports for API views and responses
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
# Token model for login/retrieval
from rest_framework.authtoken.models import Token
# Our serializers
from .serializers import RegisterSerializer, LoginSerializer
# Create your views here.
from rest_framework.permissions import AllowAny, IsAuthenticated

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