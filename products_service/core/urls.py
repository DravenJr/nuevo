
from django.urls import path
from . import views

urlpatterns = [
    path('health/', views.health),
    path('categories/', views.CategoryListCreate.as_view()),
    path('categories/<int:pk>/', views.CategoryRetrieveUpdateDestroy.as_view()),
    path('products/', views.ProductListCreate.as_view()),
    path('products/<int:pk>/', views.ProductRetrieveUpdateDestroy.as_view()),
]
