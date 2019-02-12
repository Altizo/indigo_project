from snowpenguin.django.recaptcha2.fields import ReCaptchaField
from snowpenguin.django.recaptcha2.widgets import ReCaptchaWidget
from django import forms

class ContactForm(forms.Form):
    fio = forms.CharField(max_length = 100)
    sender = forms.EmailField()
    tel = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)
    captcha = ReCaptchaField(widget=ReCaptchaWidget())
