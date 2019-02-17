from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse
from django.core.mail import send_mail

from .forms import ContactForm


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            sender = form.cleaned_data['sender']
            fio = form.cleaned_data['fio']
            tel = form.cleaned_data['tel']
            message = form.cleaned_data['message']
            copy = False

            recipients = ['reklamaindigo@gmail.com']
            # Если пользователь захотел получить копию себе, добавляем его в список получателей
            if copy:
                recipients.append(sender)
            try:
                text = 'Имя: %s \nНомер телефона: %s \nСообщение: \n%s' % (str(fio), str(tel), str(message))
                send_mail('Письмо с сайта RA-INDIGO.RU', text, settings.EMAIL_HOST_USER, recipients,
                          fail_silently=False)
            except ValueError as e:
                print("Сведения об исключении", e)
            # Переходим на другую страницу, если сообщение отправлено
            return render(request, 'thanks.html')
        else:
            return HttpResponse('Ошибка валидации письма')
    else:
        # Заполняем форму
        form = ContactForm()
    # Отправляем форму на страницу
    return render(request, 'contact.html', {'form': form})
