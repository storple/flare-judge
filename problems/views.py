from django.http import HttpResponse, HttpRequest, QueryDict
from django.core.paginator import Paginator

from django.shortcuts import render
from flare.shortcuts import htmx_render, full_page_render

from .models import Problem

def filter_problems(request: HttpRequest,data: QueryDict):
    min_elo = data.get("min_elo","")
    max_elo = data.get("max_elo","")
    tags = data.get("tags","")
    not_completed = data.get("not_completed","") != ""
    completed = data.get("completed","") != ""
    name_sort = data.get("name_sort","0")
    elo_sort = data.get("elo_sort","0")
    page = data.get("page","1")

    try:
        page = int(page)
    except:
        page = 1

    name_sort = name_sort if name_sort in ["0","1","2"] else "0"
    elo_sort = elo_sort if elo_sort in ["0","1","2"] else "0"

    if name_sort != "0" and elo_sort != "0":
        # only order by one
        name_sort = "0"

    name_sort_dict = {
        "0":"",
        "1":"problem_name",
        "2":"-problem_name",
    }
    elo_sort_dict = {
        "0":"",
        "1":"elo",
        "2":"-elo",
    }

    name_sort_field = name_sort_dict[name_sort]
    elo_sort_field  = elo_sort_dict[elo_sort]

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
    else:
        problems = Problem.objects.all()

    if min_elo != "": problems = problems.filter(elo__gte=min_elo)
    if max_elo != "": problems = problems.filter(elo__lte=max_elo)
    if tags != "": problems = problems.filter(tags__tag_name__contains=tags)

    if name_sort_field != "":
        problems = problems.order_by(name_sort_field)
    if elo_sort_field != "":
        problems = problems.order_by(elo_sort_field)

    paginator = Paginator(problems,30)
    max_pages = paginator.num_pages

    page = min(max_pages, page)

    problems = paginator.get_page(page)

    page_range = paginator.get_elided_page_range(page,on_each_side=1, on_ends=1)

    context = {
        "problems": problems,

        "min_elo": min_elo,
        "max_elo": max_elo,
        "tags": tags,

        "not_completed": not_completed,
        "completed": completed,
        
        "name_sort": name_sort,
        "elo_sort": elo_sort,

        "problem_page": page,
        "max_pages": max_pages,
        "page_range": page_range,
    }
    return context

def problems_view(request: HttpRequest):
    if request.method == "GET":
        data = request.GET

        data_present = len(data) != 0

        if data_present:
            context = filter_problems(request,data)

            if request.htmx:
                # on filter url with htmx: only return the table
                context["oob_swap"] = True
                return render(request, "problems/components/table_update.html", context)
            else:
                # on filter url without htmx: return the whole page with the filtering
                return full_page_render(request, "problems/problems.html", context, page = "problems")
        else:
            problems = Problem.objects.all()

            paginator = Paginator(problems,30)
            max_pages = paginator.num_pages

            page = 1
            problems = paginator.get_page(page)

            page_range = paginator.get_elided_page_range(page,on_each_side=1, on_ends=1)

            context = {
                "problems": problems,
                "not_completed": True,
                "completed": True,
                "name_sort": 0,
                "elo_sort": 0,

                "problem_page": page,
                "max_pages": max_pages,
                "page_range": page_range,
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
