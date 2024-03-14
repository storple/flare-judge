from django.contrib import admin

from .models import Problem
from .models import Profile
from .models import Tag

admin.site.register(Problem)
admin.site.register(Profile)
admin.site.register(Tag)
