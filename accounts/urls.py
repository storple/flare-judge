from django.urls import path
from django.contrib.auth import views as auth_views

from . import views
urlpatterns = [
    path("profile/",views.profile, name="profile"),
    path("create_profile/", views.create_profile, name="create_profile"),
    path("login/", views.login_view, name = "login"),
    # path("login/", auth_views.LoginView.as_view( template_name = "accounts/login.html", extra_context={"base_template":"base/base_navbar.html"}), name = "login"),
    path("logout/", views.logout_view, name = "logout"),
    path("change_password/",
        auth_views.PasswordChangeView.as_view(
            template_name = "accounts/change_password.html",
            success_url = "login",
            ),
        name = "change_password"),
]
