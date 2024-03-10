from django.db import models
# Create your models here.

class Tag(models.Model):
    tag_name = models.CharField(default="",max_length=200)
    def __str__(self):
        return self.tag_name

class Problem(models.Model):
    problem_name = models.CharField(default="",max_length=200)
    link = models.CharField(default="",max_length=250)
    elo = models.IntegerField(default=0)
    tags = models.ManyToManyField(Tag)
    editorial = models.CharField(default="",max_length=250)
    def __str__(self):
        return self.problem_name

class User(models.Model):
    username = models.CharField(max_length=50)
    date_joined = models.DateTimeField("date joined")
    problems_solved = models.ManyToManyField(Problem)
    def __str__(self):
        return self.username
