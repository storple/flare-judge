from django.shortcuts import render

def contests(request):
    return render(request, "base/contests.html")
