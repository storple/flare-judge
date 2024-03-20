from django.db import models

from problems.models import Problem

from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    problems_solved = models.ManyToManyField(Problem,blank=True)
    def __str__(self):
        return self.user.username
