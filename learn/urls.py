from django.urls import path

from . import views

urlpatterns = [
    path("", views.main_page, name = "learn"),
    path("guide/<slug:guide>/", views.guide_page, name = "guide"),
    path("page/<slug:page>/", views.page, name = "page"),
]
