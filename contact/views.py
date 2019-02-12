from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse
from django.core.mail import send_mail, BadHeaderError

from .forms import ContactForm

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            sender = form.cleaned_data['sender']
            message = form.cleaned_data['message']
            copy = True

            recepients = ['reklamaindigo@gmail.com']
            #Если пользователь захотел получить копию себе, добавляем его в список получателей
            if copy:
                recepients.append(sender)
            try:
                send_mail('Письмо с сайта RA-INDIGO.RU', 'Содержимое письма.', settings.EMAIL_HOST_USER, recepients, fail_silently=False)
            except BadHeaderError:
                return HttpResponse('Проблема с заголовком')
            #Переходим на другую страницу, если сообщение отправлено
            return render(request, 'thanks.html')
    else:
        #Заполняем форму
        form = ContactForm()
    #Отправляем форму на страницу
    return render(request, 'contact.html', {'form': form})
