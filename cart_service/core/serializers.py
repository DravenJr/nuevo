from rest_framework import serializers
from .models import CartItem

class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ['id', 'product_id', 'product_name', 'unit_price', 'quantity']
