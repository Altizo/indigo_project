from django.db import models
from ckeditor.fields import RichTextField
from django.utils import timezone

# Create your models here.
class infoPages(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=20, null=True, verbose_name='Заголовок')
    text = RichTextField(null=True, verbose_name='Описание')
    alias = models.CharField(max_length=10, null=True, verbose_name='Псевдоним для системы')
    edit_date = models.DateTimeField(
            default=timezone.now)

    class Meta:
        verbose_name = 'Описание информационных страниц'
        verbose_name_plural = 'Описание информационных страниц'

    def publish(self):
        self.edit_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
