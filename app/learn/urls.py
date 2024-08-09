from django.urls import path

from . import views

urlpatterns = [
    path("", views.main_page, name = "learn"),
    path("editor/", views.markdown_editor, name = "markdown_editor"),
    path("markdown_generator/", views.markdown_generator, name = "markdown_generator"),
    path("guide/<slug:guide>/", views.guide_page, name = "guide"),
    path("page/<slug:page>/", views.page, name = "page"),
]
