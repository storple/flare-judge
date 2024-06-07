from django.http import HttpResponse, HttpRequest, QueryDict

from flare.shortcuts import htmx_render, partial_render, full_render

from .models import Problem

def problems_by_page(problems: Problem, page, problem_per_page=50):
    if page >= 1:
        return problems[(page-1) * problem_per_page : page * problem_per_page]
    else:
        return None


def max_pages(problems: Problem, problems_per_page=50):
        return max(1, ((len(problems) - 1) // problems_per_page) + 1)


def filter_problems(request: HttpRequest,data: QueryDict, page):
        problems = Problem.objects.all()

        min_elo = data.get("min_elo","")
        max_elo = data.get("max_elo","")
        tags = data.get("tags","")
        completed = data.get("completed")

        if completed is not None:
            user = request.user
            if user.is_authenticated:
                currentprofile = user.profile
                problems = currentprofile.problems_solved.all()
                # problems = problems.filter(profile=currentprofile)
        # else:
            # problems = problems.objects.exclude(profile=currentprofile)

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
            "completed": completed,
            "page": page,
            "max_pages": current_max_pages,
        }

        return context

def problems_view(request: HttpRequest, page=1):
    if request.method == "GET":
        data = request.GET

        data_present = len(data) != 0

        if data_present:
            context = filter_problems(request,data,page)

            if request.htmx:
                # on filter url with htmx: only return the table
                return partial_render(request, "problems/problems&filter.html", context)
            else:
                # on filter url without htmx: return the whole page with the filtering
                return full_render(request, "problems/problems.html", context)
        else:
            problems = Problem.objects.all()

            current_max_pages = max_pages(problems)

            page = min(current_max_pages, page)

            problems = problems_by_page(problems,page)

            context = {
                "problems": problems,
                "page": page,
                "max_pages": current_max_pages,
            }
            print(context)
            return htmx_render(request, "problems/problems.html", context)
    else:
        #invalid method
        return HttpResponse(status=400)


def save_problem(request: HttpRequest):
    if request.method == "POST":
        data = request.POST
        user = request.user
        if user.is_authenticated:
            currentProfile = user.profile
            print()
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
