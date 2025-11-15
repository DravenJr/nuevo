from django.urls import path
from .views import OrderListCreateView, OrderRetrieveUpdateDestroyView

urlpatterns = [
    # Listar todas las órdenes y crear una nueva
    path('orders/', OrderListCreateView.as_view(), name='order-list-create'),

    # Obtener, actualizar o eliminar una orden específica
    path('orders/<int:pk>/', OrderRetrieveUpdateDestroyView.as_view(), name='order-detail'),
]
