from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken

from .serializers import RegisterSerializer, LoginSerializer


class RegisterView(APIView):
    def post(self, request):
        
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        return Response(
            {
                "id": user.id,
                "email": user.email,
            },
            status=status.HTTP_201_CREATED,
        )


class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)

        if not serializer.is_valid():
            
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST,
            )

        user = serializer.validated_data

        refresh = RefreshToken.for_user(user)

        return Response(
            {
                "access": str(refresh.access_token),
                "refresh": str(refresh),
                "user": {
                    "id": user.id,
                    "email": user.email,
                    "full_name": user.full_name,
                },
            },
            status=status.HTTP_200_OK,
        )
