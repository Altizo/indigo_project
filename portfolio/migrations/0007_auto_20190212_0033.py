# Generated by Django 2.1.5 on 2019-02-11 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0006_auto_20190211_1147'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='hidden',
        ),
        migrations.AddField(
            model_name='project',
            name='show',
            field=models.BooleanField(default=False, verbose_name='Показывать этот проект на сайте'),
        ),
        migrations.AlterField(
            model_name='preview',
            name='full_size',
            field=models.ImageField(upload_to='portfolio/full_size/', verbose_name='Оригинал'),
        ),
        migrations.AlterField(
            model_name='preview',
            name='thumbs',
            field=models.ImageField(upload_to='portfolio/thumbs/', verbose_name='Превью 200х200px'),
        ),
    ]
