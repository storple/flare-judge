from django.db import models

class Tag(models.Model):
    tag_name = models.CharField(default="",max_length=200)
    def __str__(self):
        return self.tag_name

class Problem(models.Model):
    problem_name = models.CharField(default="",max_length=200)
    link = models.CharField(default="",max_length=250)
    elo = models.IntegerField(default=0)
    tags = models.ManyToManyField(Tag,blank=True)
    editorial = models.CharField(default="",blank=True,max_length=250)
    def __str__(self):
        return self.problem_name
