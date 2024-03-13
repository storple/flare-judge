from django.urls import path
from django.contrib.auth import views as auth_views

from . import views
urlpatterns = [
    path("profile/",views.profile, name="profile"),
    path("createProfile/", views.createProfile, name="createProfile"),
    path("login/",
         auth_views.LoginView.as_view(
             template_name = "accounts/login.html",
             next_page = "profile",
         ),
         name = "login"),
    path("logout/",
         auth_views.LogoutView.as_view(
             template_name = "accounts/logout.html",
             next_page = "home"
             ),
         name = "logout"),
]
