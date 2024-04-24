from django.urls import path

from . import views

urlpatterns = [
    path("", views.problems, name = "problems"),
    path("page/<int:page>/", views.problems, name = "problems_page"),
    path("save_problem/", views.save_problem, name = "save_problem"),

]
