from django.shortcuts import render

from .models import Guide, Page

def main_page(request):
    guides = Guide.objects.all()
    context = {
        "guides": guides
    }

    return render(request, "learn/main_page.html", context)

def guide_page(request,guide=None):
    if guide is not None:
        try:
            currentGuide = Guide.objects.get(safe_guide_name=guide)
        except:
            currentGuide = None
        context = {
            "guide": currentGuide
        }
        return render(request, "learn/guide_page.html", context)

def page(request,page=None):
    if page is not None:
        try:
            currentPage = Page.objects.get(safe_page_name=page)
        except:
            currentPage = None

        context = {
            "page": currentPage
        }
        return render(request, "learn/page.html", context)
