from django.contrib import admin

from .models import Problem
from .models import UserInfo
from .models import Tag

admin.site.register(Problem)
admin.site.register(UserInfo)
admin.site.register(Tag)
