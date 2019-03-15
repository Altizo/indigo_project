from django.shortcuts import render
from django.http import HttpResponse

from .models import Settings


def coming_soon(arg):
    start_date = Settings.objects.values('start_date').get(pk=1)
    return render(arg, 'coming_soon.html', {'start_date': start_date})
