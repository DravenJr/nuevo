from django.urls import path
from .views import CartListCreateView, CartDetailView

urlpatterns = [
    path('cart/', CartListCreateView.as_view(), name='cart-list-create'),
    path('cart/<int:id>/', CartDetailView.as_view(), name='cart-detail'),
]
