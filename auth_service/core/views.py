from rest_framework import generics, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import RegisterSerializer, LoginSerializer
from .rabbitmq import send_user_created_message

User = get_user_model()

class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    queryset = User.objects.all()
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        # Si ya está logueado → no puede registrarse
        if request.user and request.user.is_authenticated:
            return Response(
                {"detail": "Ya estás autenticado. No puedes registrarte."},
                status=status.HTTP_400_BAD_REQUEST
            )
        return super().post(request, *args, **kwargs)

    def perform_create(self, serializer):
        user = serializer.save()
        send_user_created_message(user)  # Envía evento a RabbitMQ

class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        # Si ya está logueado → no puede loguearse otra vez
        if request.user and request.user.is_authenticated:
            return Response(
                {"detail": "Ya estás autenticado."},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]

        # Generar tokens JWT
        refresh = RefreshToken.for_user(user)

        return Response({
            "access": str(refresh.access_token),
            "refresh": str(refresh),
            "user": {
                "id": user.id,
                "username": user.username,
                "email": user.email
            }
        })

class LogoutView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]  # Solo usuarios logueados

    def post(self, request):
        # requiere que envíes el refresh token
        refresh_token = request.data.get("refresh")

        if not refresh_token:
            return Response(
                {"detail": "Debes enviar el refresh token."},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            token = RefreshToken(refresh_token)
            token.blacklist()  # invalidamos el token
            return Response({"detail": "Logout exitoso."})
        except Exception:
            return Response(
                {"detail": "Token inválido."},
                status=status.HTTP_400_BAD_REQUEST
            )