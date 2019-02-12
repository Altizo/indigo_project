from django.db import models
from django.utils import timezone


class price_OffsetPress(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название продукции')
    price1000 = models.CharField(max_length=5, blank=True, verbose_name='1000шт')
    price2000 = models.CharField(max_length=5, blank=True, verbose_name='2000шт')
    price5000 = models.CharField(max_length=5, blank=True, verbose_name='5000шт')
    edit_date = models.DateTimeField(
        default=timezone.now)

    class Meta:
        verbose_name = 'Цены по офсетной печати'
        verbose_name_plural = 'Цены по офсетной печати'

    def __str__(self):
        return self.name


class price_LargeFormatPress(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название продукции')
    category = models.CharField(max_length=200, verbose_name='Категория')
    cost = models.CharField(max_length=5, verbose_name='Цена')
    edit_date = models.DateTimeField(
        default=timezone.now)

    class Meta:
        verbose_name = 'Цены по широкоформатной печати'
        verbose_name_plural = 'Цены по широкоформатной печати'

    def __str__(self):
        return self.name


class price_Design(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название услуги')
    cost = models.CharField(max_length=5, verbose_name='Цена')
    edit_date = models.DateTimeField(
        default=timezone.now)

    class Meta:
        verbose_name = 'Цены за дизайн'
        verbose_name_plural = 'Цены за дизайн'

    def __str__(self):
        return self.name
