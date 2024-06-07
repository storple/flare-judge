from django.shortcuts import render, redirect
from django_htmx.http import HttpResponseLocation

# template is only content (body) if the page, while full template is the whole page
def htmx_render(request,template,context={}):
    if request.htmx:
        base_template = "_partial.html"
    else:
        base_template = "base/base_navbar.html"
    context.update({ "base_template": base_template })
    return render(request,template,context)

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
