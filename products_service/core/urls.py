from django.urls import path
from .views import (CategoryListCreate, CategoryRetrieveUpdateDestroy, CategoryProductsList, ProductListCreate, ProductRetrieveUpdateDestroy
)

urlpatterns = [
    # Categorías
    path('categories/', CategoryListCreate.as_view()),
    path('categories/<int:pk>/', CategoryRetrieveUpdateDestroy.as_view()),
    path('categories/<int:category_id>/products/', CategoryProductsList.as_view()),

    # Productos
    path('products/', ProductListCreate.as_view()),
    path('products/<int:pk>/', ProductRetrieveUpdateDestroy.as_view()),
]
