from django.db import models
from django.contrib.auth.models import User

class Tag(models.Model):
    tag_name = models.CharField(default="",max_length=200)
    def __str__(self):
        return self.tag_name

class Problem(models.Model):
    problem_name = models.CharField(default="",max_length=200)
    link = models.CharField(default="",max_length=250)
    elo = models.IntegerField(default=0)
    tags = models.ManyToManyField(Tag,blank=True)
    editorial = models.CharField(default="",max_length=250)
    def __str__(self):
        return self.problem_name

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    problems_solved = models.ManyToManyField(Problem,blank=True)
    def __str__(self):
        return self.user.username
