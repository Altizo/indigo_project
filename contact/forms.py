from django import forms
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV3


class ContactForm(forms.Form):
    fio = forms.CharField(max_length=100)
    sender = forms.EmailField()
    tel = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)
    captcha = ReCaptchaField(public_key='6LcTS5EUAAAAAOkX4wSfW2KRBpCFqk1d34XfKpzE',
                             private_key='6LcTS5EUAAAAACQEdTyhM6W6DGqtbxDEkjphRg1s',
                             widget=ReCaptchaV3(),
                             )
