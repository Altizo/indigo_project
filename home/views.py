from django.shortcuts import render

# Create your views here.
def home(arg):
    return render(arg, 'home.html', {})
