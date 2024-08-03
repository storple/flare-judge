from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse, Http404, HttpResponseNotAllowed, HttpResponseBadRequest, HttpResponseForbidden
from django.shortcuts import get_object_or_404
from flare.shortcuts import htmx_render

from .models import Guide, Page

from problems.models import Problem

from .markdown import md

@login_required
def markdown_generator(request):
    if request.method == "POST":
        if not request.user.has_perm('learn.change_page'):
            return HttpResponseForbidden()

        data = request.POST
        markdown = data.get("editor","")

        if markdown == "": return HttpResponseBadRequest()

        html_generated = md.convert(markdown)
        return HttpResponse(html_generated)
    else:
        return HttpResponseNotAllowed(['POST'])

@login_required
def markdown_editor(request):
    if not request.user.has_perm('learn.change_page'):
        raise PermissionDenied
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
    if guide is None:
        # maybe return to home page?
        raise Http404("Guide not given")

    currentGuide = get_object_or_404(Guide,url_name=guide)

    user = request.user

    if user.is_authenticated:
        view_page_perm = user.has_perm('learn.view_page')
        view_guide_perm = user.has_perm('learn.view_guide')
    else:
        view_page_perm = False
        view_guide_perm = False

    guide_view_permission = currentGuide.visible or view_guide_perm

    if not guide_view_permission:
        raise PermissionDenied

    if view_page_perm:
        # can view all the pages
        pages = currentGuide.page_set.all()
    else:
        pages = currentGuide.page_set.filter(visible=True)

    context = {
        "guide": currentGuide,
        "pages": pages
    }
    return htmx_render(request, "learn/guide_page.html", context, page="learn")

def page(request,page=None):
    # problems = Problem.objects.all()
    if page is None:
        raise Http404("Page not given")

    currentPage = get_object_or_404(Page,url_name=page)

    user = request.user

    if user.is_authenticated:
        view_page_perm = user.has_perm('learn.view_page')
        view_guide_perm = user.has_perm('learn.view_guide')
    else:
        view_page_perm = False
        view_guide_perm = False

    currentPage_view_permission = currentPage.visible or view_page_perm
    if not (currentPage_view_permission):
        raise PermissionDenied

    guide = currentPage.guide

    if guide is None:
        pages = [ currentPage ]
        page_order = 1
        previous_page = None
        next_page = None
        guide_view_permission = False
    else:
        if view_page_perm:
            # can view all the pages
            pages = guide.page_set.all()
        else:
            pages = guide.page_set.filter(visible=True)

        # since there is a small amount of pages per guide these operations are not expensive
        page_order = currentPage.page_order
        previous_page = pages.filter(page_order__lt=page_order).last()
        next_page = pages.filter(page_order__gt=page_order).first()

        guide_view_permission = guide.visible or view_guide_perm

    context = {
        "page": currentPage,
        "pages": pages,
        "next_page": next_page,
        "previous_page": previous_page,
        "guide_view_permission": guide_view_permission
        #"problems": problems
    }
    return htmx_render(request, "learn/page.html", context, page="learn")
