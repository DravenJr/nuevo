from rest_framework import generics
from .models import Cart, CartItem
from .serializers import GenericSerializer

# Listar y crear Carritos
class CartListCreateView(generics.ListCreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = GenericSerializer

    def get_queryset(self):
        user_id = self.request.query_params.get('user_id')
        if user_id:
            return self.queryset.filter(user_id=user_id)
        return self.queryset

# Detalle, actualizar o eliminar un carrito
class CartDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cart.objects.all()
    serializer_class = GenericSerializer
    lookup_field = 'id'
