from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name = "home"),
    # path("404", views.testview_404),
    # path("500", views.testview_500),
    # path("403", views.testview_403),
    # path("400", views.testview_400),
]
