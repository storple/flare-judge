from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from flare.shortcuts import htmx_render

from .models import Guide, Page

from problems.models import Problem

from .markdown import md

@login_required
def markdown_generator(request):
    if request.method == "POST":
        if request.user.is_superuser: # just using request.user attributes
            data = request.POST
            markdown = data.get("editor","")
            if markdown == "":
                return HttpResponse()
            else:
                html_generated = md.convert(markdown)
                return HttpResponse(html_generated)
        else:
            # forbidden
            return HttpResponse(status=403)
    else:
        # method invalid
        return HttpResponse(status=400)


def markdown_editor(request):
    return htmx_render(request, "learn/markdown_editor.html", page="learn")

def main_page(request):
    guides = Guide.objects.filter(in_main_page=True)
    pages = Page.objects.filter(in_main_page=True)
    context = {
        "guides": guides, 
        "pages": pages 
    }
    return htmx_render(request, "learn/main_page.html", context, page="learn")

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
        return htmx_render(request, "learn/guide_page.html", context, page="learn")

def page(request,page=None):
    problems = Problem.objects.all()
    if page is not None:
        try:
            currentPage = Page.objects.get(url_name=page)
        except:
            currentPage = None

        if currentPage is not None:
            page_order = currentPage.page_order
            guide = currentPage.guide
            pages = guide.page_set.filter(visible=True)
            previous_page = pages.filter(page_order__lt=page_order).last()
            next_page = pages.filter(page_order__gt=page_order).first()

        context = {
            "page": currentPage,
            "pages": pages,
            "next_page": next_page,
            "previous_page": previous_page,
            "problems": problems
        }
        return htmx_render(request, "learn/page.html", context ,page="learn")
