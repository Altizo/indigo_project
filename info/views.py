from django.shortcuts import render
from .models import infoPages

def info(arg):
    return render(arg, 'base.html', {})

def infoPress(arg):
    textPacked = infoPages.objects.get(alias='press')
    return render(arg, 'press.html', {'textPacked': textPacked})
def infoBrending(arg):
    textPacked = infoPages.objects.get(alias='brending')
    return render(arg, 'brending.html', {'textPacked': textPacked})
def infoRazmeshenie(arg):
    textPacked = infoPages.objects.get(alias='razm')
    return render(arg, 'razmeshenie.html', {'textPacked': textPacked})
def infoWeb(arg):
    textPacked = infoPages.objects.get(alias='web')
    return render(arg, 'web.html', {'textPacked': textPacked})
def infoDesign(arg):
    textPacked = infoPages.objects.get(alias='design')
    return render(arg, 'design.html', {'textPacked': textPacked})
