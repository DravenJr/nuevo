import requests
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

def index(request):
    return render(request, "index.html")

# Mapeo de servicios internos
CONTAINERS = {
    "auth": "http://auth_service:8000",
    "products": "http://products_service:8000",
    "cart": "http://cart_service:8000",
    "orders": "http://orders_service:8000",
}

def proxy_request(request, service_name, path=""):
    if service_name not in CONTAINERS:
        return JsonResponse({"error": "Servicio no encontrado"}, status=404)
    
    url = f"{CONTAINERS[service_name]}/{path}"
    
    try:
        resp = requests.request(
            method=request.method,
            url=url,
            headers={k: v for k, v in request.headers.items() if k != 'Host'},
            data=request.body,
            params=request.GET,
            timeout=10
        )
    except requests.exceptions.RequestException as e:
        return JsonResponse({"error": str(e)}, status=500)
    
    response = HttpResponse(resp.content, status=resp.status_code)
    for key, value in resp.headers.items():
        response[key] = value
    return response

