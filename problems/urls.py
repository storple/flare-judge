from django.urls import path

from . import views

urlpatterns = [
    path("", views.problems, name = "problems"),
    path("save_progress", views.save_progress, name = "save_progress"),
    path("<int:min_elo>/<int:max_elo>/<int:completed>/", views.problems),
    path("<int:min_elo>/<int:max_elo>/<int:completed>/<slug:tags>/", views.problems, name = "search_problems"),

]
