from django.shortcuts import render

# Create your views here.
from .models import Settings


def coming_soon(arg):
    return render(arg, 'base.html', {})
