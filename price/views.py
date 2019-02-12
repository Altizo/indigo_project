from django.shortcuts import render
from .models import price_OffsetPress, price_LargeFormatPress, price_Design

# Create your views here.
def all(arg):
    price_OffsetPress_Packed = price_OffsetPress.objects.all()
    price_LargeFormatPress_Packed = price_LargeFormatPress.objects.all()
    price_Design_Packed = price_Design.objects.all()
    return render(arg, 'price.html', {'price_OffsetPress': price_OffsetPress_Packed,
                                        'price_LargeFormatPress': price_LargeFormatPress_Packed,
                                        'price_Design': price_Design_Packed})

def press(arg):
    price_OffsetPress_Packed = price_OffsetPress.objects.all()
    price_LargeFormatPress_Packed = price_LargeFormatPress.objects.all()
    return render(arg, 'price_press.html', {'price_OffsetPress': price_OffsetPress_Packed,
                                        'price_LargeFormatPress': price_LargeFormatPress_Packed})

def brending(arg):
    return render(arg, 'price_brending.html', {})

def razm(arg):
    return render(arg, 'price_razm.html', {})

def web(arg):
    return render(arg, 'price_web.html', {})

def design(arg):
    price_Design_Packed = price_Design.objects.all()
    return render(arg, 'price_design.html', {'price_Design': price_Design_Packed})
