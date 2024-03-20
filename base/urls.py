from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name = "home"),
    path("learn", views.learn, name = "learn"),
    path("contests", views.contests, name = "contests"),
]
