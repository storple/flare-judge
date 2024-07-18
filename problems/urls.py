from django.urls import path

from . import views

urlpatterns = [
    path("", views.problems_view, name = "problems"),
    # path("page/<int:page>/", views.problems, name = "problems_page"),
    # path("page/<int:page>/", views.filter_problems, name = "problems_page"),
    # path("page/<int:problem_page>/", views.problems_view, name = "problems_page"),
    path("save_problem/", views.save_problem, name = "save_problem"),
]
