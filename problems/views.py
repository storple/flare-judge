from django.shortcuts import render
from django.http import HttpResponse

from .models import Problem

def problems_by_page(problems,page,problem_per_page):
    if page >= 1:
        return problems[(page-1) * problem_per_page : page * problem_per_page]
    else:
        return None

def problems(request, page=1, problem_per_page=50):
    problems = Problem.objects.all()

    # called on a page change or filtering change
    if request.method == "POST":
        data = request.POST
        min_elo = data.get("min_elo","")
        max_elo = data.get("max_elo","")
        tags = data.get("tags","")
        completed = data.get("completed")
        # problem_per_page = data.get("problem_per_page",3)

        if completed is not None:
            user = request.user
            if user.is_authenticated:
                currentProfile = user.profile
                problems = currentProfile.problems_solved.all()
                # problems = problems.filter(profile=currentProfile)
        # else:
            # problems = problems.objects.exclude(profile=currentProfile)

        if min_elo != "": problems = problems.filter(elo__gte=min_elo)
        if max_elo != "": problems = problems.filter(elo__lte=max_elo)
        if tags != "": problems = problems.filter(tags__tag_name__contains=tags)

        problems = problems_by_page(problems,page,problem_per_page)

        context = {
            "problems": problems,
            "page": page,
            "min_elo": min_elo,
            "max_elo": max_elo,
            "tags": tags,
            "completed": completed,
        }
        return render(request, "problems/problems&filter.html", context)

    #first rendering of the page
    problems = problems_by_page(problems,page,problem_per_page)
    context = {
        "problems": problems,
        "page": page
    }
    return render(request, "problems/problems.html", context)


def save_problem(request):
    if request.method == "POST":
        data = request.POST
        user = request.user
        if user.is_authenticated:
            currentProfile = user.profile
            print()
            name = data["name"]
            try:
                problem = Problem.objects.get(problem_name=name)
                problems_solved = currentProfile.problems_solved.all()
                if data.get(name) is not None:
                    # checkbox is on
                    if problem not in problems_solved:
                        currentProfile.problems_solved.add(problem)
                else:
                    # checkbox is off
                    if problem in problems_solved:
                        currentProfile.problems_solved.remove(problem)
            except:
                #triggers when the given problem name is invalid(or if another error occurs)
                return HttpResponse(status=400)
            # response went well
            return HttpResponse(status=200)
        # user not authenticated
        return HttpResponse(status=401)
    # method invalid
    return HttpResponse(status=400)
