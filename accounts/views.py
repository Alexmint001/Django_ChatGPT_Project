from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializers import RegisterSerializer, LoginSerializer
from rest_framework.response import Response
from rest_framework import generics, status
from django.contrib.auth.models import User

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

userregister = RegisterView.as_view()

class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        return Response({
            'token': data['token'].key,
            'username': data['username'],
            'email': data['email'],
        }, status=status.HTTP_200_OK)
    
userlogin = LoginView.as_view()

class ProfileView(generics.GenericAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        return Response({
            'username': request.user.username,
            'email': request.user.email,
        })
    
userprofile = ProfileView.as_view()