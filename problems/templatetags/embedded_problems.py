from django import template
from problems.models import Problem

register = template.Library()

@register.inclusion_tag("problems/problems_table.html")
def embed_problem(problem_name):
    problem = Problem.objects.filter(problem_name=problem_name)
    return {"problems":problem}

@register.inclusion_tag("problems/problems_table.html")
def embed_problems(*args):
    problem = Problem.objects.filter(problem_name__in=args)
    return {"problems":problem}
