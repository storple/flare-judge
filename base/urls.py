from django.urls import path

from . import views

urlpatterns = [
    path("", views.home),
    path("home", views.home, name = "home"),
    path("problems", views.problems, name = "problems"),
    path("learn", views.learn, name = "learn"),
    path("contests", views.contests, name = "contests"),
    path("login", views.login, name = "login"),
    path("signup", views.signup, name = "signup"),
]
