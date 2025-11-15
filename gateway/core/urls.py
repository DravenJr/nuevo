from django.urls import path
from .views import index, proxy_request

urlpatterns = [
    path('', index, name='index'),
    path('auth/<path:path>/', lambda r, path: proxy_request(r, "auth", path)),
    path('products/<path:path>/', lambda r, path: proxy_request(r, "products", path)),
    path('cart/<path:path>/', lambda r, path: proxy_request(r, "cart", path)),
    path('orders/<path:path>/', lambda r, path: proxy_request(r, "orders", path)),
]
