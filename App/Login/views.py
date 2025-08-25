from django.shortcuts import render
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import viewsets,status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from .serializers import CustomTokenObtainPairSerializer

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

class LogoutView(APIView):
        def post(self, request):
            try:
                refresh_token = request.data['refresh']
                token = RefreshToken(refresh_token)
                token.blacklist()
                return Response({"logout exitoso":"saliendo"}, status=status.HTTP_200_OK)
            except Exception as ex:
                return Response({"error":"token invalido"}, status=status.HTTP_400_BAD_REQUEST)









# class loginApiView(APIView):
#     def create_token(self, request):
#         username = request.data.get('username')
#         password = request.data.get('password')

#         user = authenticate(username=username, password=password)

#         if user is not None:
#             refresh = RefreshToken.for_user(user)
#             return Response({
#                 'refresh': str(refresh),
#                 'access': str(refresh.access_token),
#                 'user_id': user.id,
#                 'username': user.username
#             }, status=status.HTTP_200_OK)
#         else:
#             return Response({'error':'credenciales invalidas'}, status=status.HTTP_401_UNAUTHORIZED)

# Create your views here.
