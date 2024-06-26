from django.shortcuts import render

from .models import Guide, Page

from problems.models import Problem

def main_page(request):
    guides = Guide.objects.filter(in_main_page=True)
    pages = Page.objects.filter(in_main_page=True)
    context = {
        "guides": guides, 
        "pages": pages 
    }
    return render(request, "learn/main_page.html", context)

def guide_page(request,guide=None):
    if guide is not None:
        try:
            currentGuide = Guide.objects.get(url_name=guide)
            pages = currentGuide.page_set.filter(visible=True)
        except:
            currentGuide = None
            pages = None
        context = {
            "guide": currentGuide,
            "pages": pages
        }
        return render(request, "learn/guide_page.html", context)

def page(request,page=None):
    problems = Problem.objects.all()
    if page is not None:
        try:
            currentPage = Page.objects.get(url_name=page)
        except:
            currentPage = None

        context = {
            "page": currentPage,
            "problems": problems
        }
        return render(request, "learn/page.html", context)
