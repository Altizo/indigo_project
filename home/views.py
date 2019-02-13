from django.shortcuts import render


def home(arg):
    return render(arg, 'home.html', {})
