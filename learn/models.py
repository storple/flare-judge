from django.db import models
from django.core.files.storage import FileSystemStorage
from django.core.files.base import ContentFile
from django.template.defaultfilters import slugify

from accounts.models import Profile

from .markdown import md

learn_page_fs = FileSystemStorage(location="learn/templates/generated")

class Guide(models.Model):
    guide_name = models.CharField(default="",max_length=200)
    url_name = models.SlugField(default=guide_name,max_length=200)
    short_description = models.TextField(default="")
    description = models.TextField(default="")
    visible = models.BooleanField(default=False)
    in_main_page  = models.BooleanField(default=False)
    def __str__(self):
        return self.guide_name

    #creates the safe url name
    def save(self, *args, **kwargs):
        self.url_name = slugify(self.guide_name)
        super().save(*args, **kwargs)


class Page(models.Model):
    page_name = models.CharField(default="",max_length=200)
    url_name = models.SlugField(default=page_name,max_length=200)
    html_template_name = models.CharField(default="",max_length=200)

    markdown = models.TextField()
    html_generated_file = models.FileField(storage=learn_page_fs, upload_to="")
    toc = models.TextField(default="")

    authors = models.ManyToManyField(Profile)
    visible = models.BooleanField(default=False)
    in_main_page  = models.BooleanField(default=False)
    guide = models.ForeignKey(
        Guide,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    def __str__(self):
        return self.page_name

    def save(self, *args, **kwargs):
        #deletes current file to avoid duplicates
        if self.html_generated_file:
            path = self.html_generated_file.path
            if learn_page_fs.exists(path):
                learn_page_fs.delete(path)

        self.url_name = slugify(self.page_name)

        #slugs are also filename-friendly, so they can be reused for that
        if self.guide is not None:
            filename = "{}/{}.html".format(self.guide.url_name,self.url_name)
        else:
            filename = "{}.html".format(self.url_name)

        #saves the generated markdown
        print("started markdowning")
        print("halfway stuff")
        html_generated = md.convert(self.markdown)
        print("now here stuff")
        self.toc = md.toc

        self.html_generated_file = ContentFile(html_generated, name=filename)

        self.html_template_name = "generated/{}".format(self.html_generated_file.name)
        print("finally")
        super().save(*args, **kwargs)
