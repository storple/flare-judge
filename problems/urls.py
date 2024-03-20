from django.urls import path

from . import views

urlpatterns = [
    path("problems", views.problems, name = "problems"),
    path("problems/<int:min_elo>/<int:max_elo>/<int:completed>/", views.problems),
    path("problems/<int:min_elo>/<int:max_elo>/<int:completed>/<slug:tags>/", views.problems, name = "search_problems"),
]
