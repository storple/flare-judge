from django.urls import path
from django.contrib.auth import views as auth_views

from . import views
urlpatterns = [
    path("profile/",views.profile, name="profile"),
    path("create_profile/", views.create_profile, name="create_profile"),
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
    path("change_password/",
        auth_views.PasswordChangeView.as_view(
            template_name = "accounts/change_password.html",
            success_url = "login",
            ),
        name = "change_password"),
]
