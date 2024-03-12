from django.shortcuts import render

# Create your views here.
from .models import Problem

def home(request):
    return render(request, "base/home.html")

def problems(request):
    problems = Problem.objects.all()
    context = {
        "problems": problems,
    }
    return render(request, "base/problems.html", context)

def contests(request):
    return render(request, "base/contests.html")

def learn(request):
    return render(request, "base/learn.html")

def signup(request):
    return render(request, "base/signup.html")

def login(request):
    return render(request, "base/login.html")
