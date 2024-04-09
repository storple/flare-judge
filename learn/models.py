from django.db import models
from django.core.files.storage import FileSystemStorage
from django.core.files.base import ContentFile

from accounts.models import Profile

import markdown

learn_page_fs = FileSystemStorage(location="learn/templates/generated")


class Guide(models.Model):
    guide_name = models.CharField(default="",max_length=200)
    safe_guide_name = models.CharField(default="",max_length=200)
    description = models.TextField()
    def __str__(self):
        return self.guide_name

class Page(models.Model):
    page_name = models.CharField(default="",max_length=200)
    safe_page_name = models.CharField(default="",max_length=200)
    authors = models.ManyToManyField(Profile)
    markdown = models.TextField()
    html_generated_file = models.FileField(storage=learn_page_fs, upload_to="")

    guide = models.ForeignKey(
        Guide,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )

    def __str__(self):
        return self.page_name

    # generates html from markdown text and saves it to a file
    def save(self, *args, **kwargs):
        #deletes current file to avoid duplicates
        if self.html_generated_file:
            path = self.html_generated_file.path
            if learn_page_fs.exists(path):
                learn_page_fs.delete(path)

        html_generated = markdown.markdown(self.markdown, output_format="html")

        if self.guide is not None:
            filename = self.guide.guide_name+"/"+self.safe_page_name+".html"
        else:
            filename = self.safe_page_name+".html"
        self.html_generated_file = ContentFile(html_generated, name=filename)
        super().save(*args, **kwargs)

