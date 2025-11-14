
from django.db import models
from django.conf import settings

class Cart(models.Model):
    user_id = models.IntegerField()  # link to auth service user id
    created_at = models.DateTimeField(auto_now_add=True)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name='items', on_delete=models.CASCADE)
    product_id = models.IntegerField()
    quantity = models.PositiveIntegerField(default=1)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
