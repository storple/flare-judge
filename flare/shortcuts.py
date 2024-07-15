from django.shortcuts import render, redirect
from django_htmx.http import HttpResponseLocation

# template is only content (body) if the page, while full template is the whole page
def partial_page_render(request,template,context={}, **kwargs):
    base_template = "_partial.html"
    current_page = kwargs.get("page","")

    context.update({ "base_template": base_template, "current_page": current_page})

    return render(request,template,context)

def full_page_render(request,template,context={}, **kwargs):
    base_template = "base/base_navbar.html"
    current_page = kwargs.get("page","")

    context.update({ "base_template": base_template, "current_page": current_page})

    return render(request,template,context)

def htmx_render(request,template,context={}, **kwargs):
    if request.htmx:
        return partial_page_render(request,template,context, **kwargs)
    else:
        return full_page_render(request,template,context, **kwargs)

# template is only content (body) if the page, to is for the redirect
def htmx_redirect(request,redirect_to, **kwargs):
    if request.htmx:
        #defaults to swapping main
        if "swap" not in kwargs:
            kwargs["swap"] = "innerHTML"
        if "target" not in kwargs:
            kwargs["target"] = "#main"
        return HttpResponseLocation(redirect_to, **kwargs)
    else:
        return redirect(redirect_to)
