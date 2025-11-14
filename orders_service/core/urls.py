
from django.urls import path
from . import views

urlpatterns = [
    path('health/', views.health),
    path('orders/', views.OrderCreateView.as_view()),
    path('orders/<int:pk>/', views.OrderDetailView.as_view()),
]
