from django.shortcuts import render

from .models import Project


def portfolio(arg):
    ctx = {
        'project_list': Project.objects.all().filter(show=True),
    }

    return render(arg, 'portfolio.html', ctx)
