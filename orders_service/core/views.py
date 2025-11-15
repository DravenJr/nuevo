from rest_framework import generics
from .models import Order
from .serializers import OrderSerializer

# Listar todas las órdenes y crear una nueva
class OrderListCreateView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

# Obtener, actualizar o eliminar una orden específica
class OrderRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
