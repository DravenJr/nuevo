from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth import get_user_model
from .serializers import RegisterSerializer

User = get_user_model()

@api_view(['GET'])
def health(request):
    return Response({'status': 'ok'})


class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    queryset = User.objects.all()
