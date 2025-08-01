# users/views.py
from django.contrib.auth.models import User
from rest_framework import serializers, generics
from rest_framework.response import Response
from rest_framework import status

from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from users.authentication import CookieTokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password']

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("A user with this email already exists.")
        return value
    
    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['email'],  # Using email as username
            email=validated_data['email'],
            password=validated_data['password'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        return user

class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        
        return Response(
            {"message": "User created successfully"},
            status=status.HTTP_201_CREATED
        )
    
class CustomLoginView(ObtainAuthToken):
    # def post(self, request, *args, **kwargs):
    #     serializer = self.serializer_class(data=request.data,
    #                                        context={'request': request})
    #     serializer.is_valid(raise_exception=True)
    #     user = serializer.validated_data['user']
    #     token, created = Token.objects.get_or_create(user=user)

    #     return Response({
    #         'message': f"User {user.email} logged in successfully",
    #         'token': token.key
    #     }, status=status.HTTP_200_OK)
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)

        response = Response({
            'message': f"User {user.email} logged in successfully",
            'token': token.key
        }, status=status.HTTP_200_OK)

        #  Set token in cookie
        response.set_cookie(
            key='auth_token',
            value=token.key,
            httponly=True,  # prevent JS access for security
            secure=True,   # True if using HTTPS
            samesite='Lax'  # Adjust based on your frontend needs
        )
        return response
    
class LogoutView(APIView):
    authentication_classes = [CookieTokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user

        # Check if user has a token
        if hasattr(user, 'auth_token'):
            user.auth_token.delete()
            response = Response({'message': 'Logged out successfully'}, status=status.HTTP_200_OK)
            response.delete_cookie('auth_token')  # Optional: clear the token from cookies
            return response
        else:
            return Response({'detail': 'Please log in first.'}, status=status.HTTP_400_BAD_REQUEST)