
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Cart, CartItem
from .serializers import GenericSerializer

class CartView(APIView):
    def get(self, request):
        return Response({'msg': 'List carts - implement filtering by user_id'})

    def post(self, request):
        return Response({'msg': 'Create cart - implement saving items'})

class CartDetailView(APIView):
    def put(self, request, cart_id):
        return Response({'msg': 'Update cart item quantities - implement'})

    def delete(self, request, cart_id):
        return Response({'msg': 'Delete cart or item - implement'})
