from django.shortcuts import render

# Create your views here.
from .models import Problem
# from .models import Tag
# from django.contrib.auth.models import User
# from accounts.models import Profile

def problems(request,min_elo=None,max_elo=None,tags=None,completed=None):
    # problems = Problem.objects.all()
    # print(min_elo,max_elo,tags,completed)
    problems = Problem.objects.all()
    # tags = Tag.objects.all()
    
    print(Problem.objects.all())
    if min_elo is not None:
        problems = problems.filter(elo__gte=min_elo)
    if max_elo is not None:
        problems = problems.filter(elo__lte=max_elo)
    if tags is not None:
        problems = Problem.objects.filter(tags__tag_name__contains=tags)
    context = {
        "problems": problems,
        # "tags": tags
    }
    return render(request, "problems/problems.html", context)
