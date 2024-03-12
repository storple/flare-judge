from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout


def log_in_request(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return render(request, "auth/success.html")
    else:
        return render(request, "auth/failure.html")

def logout_view(request):
    logout(request)
    return render(request, "auth/success.html")

def sign_up(request):
    return render(request, "auth/signup.html")

def log_in(request):
    return render(request, "auth/login.html")
