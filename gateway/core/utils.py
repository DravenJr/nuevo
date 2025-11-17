import requests

def gateway_request(request, url, method="GET", data=None):
    access = request.session.get("access")
    headers = {"Authorization": f"Bearer {access}"} if access else {}

    if method == "GET":
        return requests.get(url, headers=headers)
    elif method == "POST":
        return requests.post(url, headers=headers, json=data)
    elif method == "PUT":
        return requests.put(url, headers=headers, json=data)
    elif method == "DELETE":
        return requests.delete(url, headers=headers)
