from django.shortcuts import render

# Create your views here.
def pageMaker(request):
    return render(request, "learn/pageMaker.html")
