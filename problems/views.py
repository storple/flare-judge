from django.shortcuts import render,redirect

from .models import Problem

def problems(request,min_elo=None,max_elo=None,tags=None,completed=None):
    problems = Problem.objects.all()
    if completed is not None:
        user = request.user
        if user.is_authenticated:
            currentProfile = user.profile
            if completed == 1:
                problems = problems.filter(profile=currentProfile)
            else:
                problems = problems.exclude(profile=currentProfile)
    if min_elo is not None and min_elo != 0:
        problems = problems.filter(elo__gte=min_elo)
    if max_elo is not None and max_elo != 100000:
        problems = problems.filter(elo__lte=max_elo)
    if tags is not None:
        problems = Problem.objects.filter(tags__tag_name__contains=tags)
    context = {
        "problems": problems,
        "min_elo": min_elo,
        "max_elo": max_elo,
        "tags": tags,
        "completed": completed,
    }
    return render(request, "problems/problems.html", context)

def save_progress(request):
    if request.method == "POST":
        data = request.POST
        user = request.user
        if user.is_authenticated:
            currentProfile = user.profile

            problemsDict = data.copy()
            problemsDict.pop("csrfmiddlewaretoken")
            problemsDict.pop("save_button")

            for problem in Problem.objects.all():
                if problem.problem_name in problemsDict:
                    currentProfile.problems_solved.add(problem)
                else:
                    currentProfile.problems_solved.remove(problem)
    return redirect(problems)
