from django.urls import path

from . import views

urlpatterns = [
    path("contests", views.contests, name = "contests"),
]
