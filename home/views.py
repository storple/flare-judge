from flare.shortcuts import htmx_render

def home(request):
    # user = request.user
    # if user.is_authenticated:
    #     return htmx_render(request, "home/home.html")
    return htmx_render(request, "home/hero_home.html")

# def testview_404(request):
#     return htmx_render(request, "404.html")
# def testview_500(request):
#     return htmx_render(request, "500.html")
# def testview_403(request):
#     return htmx_render(request, "403.html")
# def testview_400(request):
#     return htmx_render(request, "400.html")
