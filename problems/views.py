from django.http import HttpResponse, HttpRequest, QueryDict

from django.shortcuts import render
from flare.shortcuts import htmx_render, full_page_render

from .models import Problem

def problems_by_page(problems: Problem, page, problem_per_page=50):
    if page >= 1:
        return problems[(page-1) * problem_per_page : page * problem_per_page]
    else:
        return None


def max_pages(problems: Problem, problems_per_page=50):
        return max(1, ((problems.count() - 1) // problems_per_page) + 1)


def filter_problems(request: HttpRequest,data: QueryDict, page):
        min_elo = data.get("min_elo","")
        max_elo = data.get("max_elo","")
        tags = data.get("tags","")
        not_completed = data.get("not_completed","") != ""
        completed = data.get("completed","") != ""

        user = request.user
        if user.is_authenticated:
                currentprofile = user.profile
                if completed and not_completed:
                    # no filtering
                    problems = Problem.objects.all()
                elif completed:
                    # only show completed ones
                    problems = currentprofile.problems_solved.all()
                elif not_completed:
                    # only show not completed problems
                    problems = Problem.objects.exclude(profile=currentprofile)
                else:
                    # no problems
                    problems = Problem.objects.none()

        if min_elo != "": problems = problems.filter(elo__gte=min_elo)
        if max_elo != "": problems = problems.filter(elo__lte=max_elo)
        if tags != "": problems = problems.filter(tags__tag_name__contains=tags)

        current_max_pages = max_pages(problems)

        page = min(current_max_pages, page)

        problems = problems_by_page(problems,page)

        context = {
            "problems": problems,
            "min_elo": min_elo,
            "max_elo": max_elo,
            "tags": tags,
            "not_completed": not_completed,
            "completed": completed,
            "problem_page": page,
            "max_pages": current_max_pages,
        }
        return context

def problems_view(request: HttpRequest, problem_page=1):
    if request.method == "GET":
        data = request.GET

        data_present = len(data) != 0

        if data_present:
            context = filter_problems(request,data,problem_page)

            if request.htmx:
                # on filter url with htmx: only return the table
                return render(request, "problems/components/problems_table.html", context)
            else:
                # on filter url without htmx: return the whole page with the filtering
                print("doing this thing")
                return full_page_render(request, "problems/problems.html", context, page = "problems")
        else:
            problems = Problem.objects.all()

            current_max_pages = max_pages(problems)

            page = min(current_max_pages, problem_page)

            problems = problems_by_page(problems,page)

            context = {
                "problems": problems,
                "problem_page": page,
                "not_completed": True,
                "completed": True,
                "max_pages": current_max_pages,
            }
            # render page without filtering
            return htmx_render(request, "problems/problems.html", context, page = "problems")
    else:
        #invalid method
        return HttpResponse(status=400)


def save_problem(request: HttpRequest):
    if request.method == "POST":
        data = request.POST
        user = request.user
        if user.is_authenticated:
            currentProfile = user.profile
            name = data["problem-name"]
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
