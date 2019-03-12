from django.db import models
from django.utils import timezone


class Settings(models.Model):
    start_date = models.DateTimeField(default=timezone.now, verbose_name='Дата проекта')
    show = models.BooleanField(default=False, verbose_name='Показывать заглушку на сайте')

    class Meta:
        verbose_name = 'настройки заглушки'
        verbose_name_plural = 'настройки заглушки'
