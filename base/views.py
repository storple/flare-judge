from django.shortcuts import render

# Create your views here.
from .models import Problem

def index(request):
    problems = Problem.objects.all()
    context = {
        "problems": problems,
    }
    return render(request, "base/index.html", context)
