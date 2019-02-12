from django.db import models
from django.utils import timezone


class Tag(models.Model):
    tag_title = models.CharField(max_length=200, verbose_name='Тег')

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = "Теги"

    def __str__(self):
        return self.tag_title


class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок проекта')
    description = models.TextField(blank=True, verbose_name='Описание')
    created_date = models.DateTimeField(default=timezone.now, verbose_name='Дата проекта')
    show = models.BooleanField(default=False, verbose_name='Показывать этот проект на сайте')

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = "Проекты"

    def __str__(self):
        return self.title


class Preview(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, verbose_name='Принадлежность к проекту')
    title = models.CharField(max_length=200, verbose_name='Заголовок изображения')
    full_size = models.ImageField(upload_to='portfolio/full_size/', verbose_name='Оригинал')
    thumbs = models.ImageField(upload_to='portfolio/thumbs/', verbose_name='Превью 200х200px')
    tag = models.ForeignKey(Tag, on_delete=models.DO_NOTHING, blank=True, verbose_name='Тег изображения')

    class Meta:
        verbose_name = 'Превью'
        verbose_name_plural = "Превью проектов"

    def __str__(self):
        return self.title
