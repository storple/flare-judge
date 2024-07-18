from django.urls import path

from . import views
from learn import views as learn_views

urlpatterns = [
    # path("", views.home, name = "home"),
    path("", learn_views.main_page, name = "home"),
]
