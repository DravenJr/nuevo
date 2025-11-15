from django.contrib import admin
from .models import Order

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'total', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('user_id',)
    ordering = ('-created_at',)
