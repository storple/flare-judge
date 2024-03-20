from django.shortcuts import render

def home(request):
    return render(request, "base/home.html")

def contests(request):
    return render(request, "base/contests.html")

def learn(request):
    return render(request, "base/learn.html")
