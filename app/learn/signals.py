from django.db.models.signals import pre_delete
from django.dispatch import receiver
from .models import Page
from .models import learn_page_fs

# deletes html file for both model and query set deletions
# setting the model's delete function only covers model deletes
# this is required for the admin page to delete them properly
@receiver(pre_delete, sender=Page)
def deletePage(sender, **kwargs):
    instance = kwargs["instance"]
    html_generated_file = instance.html_generated_file
    if html_generated_file:
        path = html_generated_file.path
        if learn_page_fs.exists(path):
            learn_page_fs.delete(path)
