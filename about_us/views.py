from django.shortcuts import render
from .models import About_us


def about_us(arg):
    about_us = About_us.objects.values('text').get(pk=1)
    return render(arg, 'about_us.html', {'about_us': about_us})
