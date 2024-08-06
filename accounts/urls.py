from django.urls import path

from . import views
urlpatterns = [
    path("profile/",views.profile, name="profile"),
    path("create_profile/", views.create_profile, name="create_profile"),
    path("login/", views.login_view, name = "login"),
    # path("login/", auth_views.LoginView.as_view( template_name = "accounts/login.html", extra_context={"base_template":"base/base_navbar.html"}), name = "login"),
    path("logout/", views.logout_view, name = "logout"),
    path("change_password/", views.ChangePasswordView.as_view(), name = "change_password"),
    path("change_password_success/", views.change_password_success_view, name = "change_password_success"),
]
