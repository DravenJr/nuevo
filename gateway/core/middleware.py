from django.shortcuts import redirect

class GatewayAuthMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        public_paths = [
            '/', '/login/', '/register/', '/static/'
        ]

        if not any(request.path.startswith(p) for p in public_paths):
            if not request.session.get("access"):
                return redirect("login")

        return self.get_response(request)
