from flare.shortcuts import htmx_render

def home(request):
    # user = request.user
    # if user.is_authenticated:
    #     return htmx_render(request, "home/home.html")
    return htmx_render(request, "home/hero_home.html")
