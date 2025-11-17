import requests
from django.shortcuts import render, redirect

def index(request):
    return render(request, "index.html")

AUTH_SERVICE = "http://auth_service:8000"

def login_view(request):
    if request.method == "GET":
        return render(request, "login.html")

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        response = requests.post(f"{AUTH_SERVICE}/login/", data={
            "username": username,
            "password": password
        })

        if response.status_code != 200:
            return render(request, "login.html", {
                "error": "Credenciales incorrectas"
            })

        data = response.json()

        # Guardar tokens en la sesión del gateway
        request.session["access"] = data["access"]
        request.session["refresh"] = data["refresh"]
        request.session["username"] = data["user"]["username"]

        return redirect("home")

def register_view(request):
    if request.method == "GET":
        return render(request, "register.html")

    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        response = requests.post(f"{AUTH_SERVICE}/register/", json={
            "username": username,
            "email": email,
            "password": password
        })

        if response.status_code != 201:
            return render(request, "register.html", {
                "error": "No se pudo registrar el usuario"
            })

        return redirect("login")

def logout_view(request):
    refresh = request.session.get("refresh")
    access = request.session.get("access")

    if refresh and access:
        try:
            requests.post(
                f"{AUTH_SERVICE}/logout/",
                data={"refresh": refresh},
                headers={"Authorization": f"Bearer {access}"}
            )
        except Exception:
            pass  # falló, pero igual cerramos sesión en el gateway

    request.session.flush()
    return redirect("home")



