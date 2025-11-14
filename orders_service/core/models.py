
from django.db import models

class Order(models.Model):
    user_id = models.IntegerField()
    total = models.DecimalField(max_digits=12, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, default='pending')
