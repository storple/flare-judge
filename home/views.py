from django.shortcuts import render

def home(request):
    user = request.user
    if user.is_authenticated:
        return render(request, "home/home.html")
    return render(request, "home/hero_home.html")
