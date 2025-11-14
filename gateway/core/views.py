
from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    # Simple HTML to show available endpoints (internal hostnames)
    html = '''
    <h1>Django Microservices Gateway</h1>
    <ul>
      <li>Auth service token: POST http://auth_service:8000/api/token/ (local: http://localhost:8001/api/token/)</li>
      <li>Products service: http://products_service:8000/api/ (local: http://localhost:8002/api/)</li>
      <li>Cart service: http://cart_service:8000/api/ (local: http://localhost:8003/api/)</li>
      <li>Orders service: http://orders_service:8000/api/ (local: http://localhost:8004/api/)</li>
    </ul>
    '''
    return HttpResponse(html)
