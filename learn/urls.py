from django.urls import path

from . import views

urlpatterns = [
    path("", views.main_page, name = "learn"),
    path("guide/<str:guide>/", views.guide_page, name = "guide"),
    path("page/<str:page>/", views.page, name = "page"),
]
