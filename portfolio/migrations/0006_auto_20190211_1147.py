# Generated by Django 2.1.5 on 2019-02-11 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0005_auto_20180529_0156'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='preview',
            options={'verbose_name': 'Превью', 'verbose_name_plural': 'Превью проектов'},
        ),
        migrations.AlterModelOptions(
            name='project',
            options={'verbose_name': 'Проект', 'verbose_name_plural': 'Проекты'},
        ),
        migrations.AlterModelOptions(
            name='tag',
            options={'verbose_name': 'Тег', 'verbose_name_plural': 'Теги'},
        ),
        migrations.AddField(
            model_name='project',
            name='hidden',
            field=models.BooleanField(default=False, verbose_name='Скрыть?'),
        ),
        migrations.AlterField(
            model_name='preview',
            name='full_size',
            field=models.ImageField(upload_to='static/img/full_size/', verbose_name='Оригинал'),
        ),
        migrations.AlterField(
            model_name='preview',
            name='thumbs',
            field=models.ImageField(upload_to='static/img/thumbs/', verbose_name='Превью 250х250px'),
        ),
    ]
