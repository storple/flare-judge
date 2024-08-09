from django.contrib import admin
from .models import Page, Guide
from django.db import models
# from .forms import PageForm
from .widgets import MarkdownEditor

class PageAdmin(admin.ModelAdmin):
    fields = ["page_name", "authors","guide","page_order","visible","in_main_page","markdown"]
    formfield_overrides = {
        models.TextField: {"widget": MarkdownEditor(attrs={"class":"hidden-textarea"})},
    }

    class Media:
        css = {
            "all": [
                "learn/markdown_editor_widget.css",
                ],
        }
        # js = ["learn/markdown_editor.js"]

class GuideAdmin(admin.ModelAdmin):
    fields = ["guide_name","visible","in_main_page","short_description","description"]

admin.site.register(Page, PageAdmin)
admin.site.register(Guide, GuideAdmin)
