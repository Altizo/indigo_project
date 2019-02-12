from django.db import models
from ckeditor.fields import RichTextField
from django.utils import timezone

# Create your models here.
class About_us(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    text = RichTextField(verbose_name='Текст о нас')

    class Meta:
        verbose_name = 'Описание страницы "О НАС"'
        verbose_name_plural = 'Описание страницы "О НАС"'

    def publish(self):
        self.edit_date = timezone.now()
        self.save()

    def __str__(self):
        title = 'Текст рассказывающий о нас'
        return title
