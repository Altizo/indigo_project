# Generated by Django 2.0.3 on 2018-05-28 20:33

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0003_auto_20180517_2159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='infopages',
            name='alias',
            field=models.CharField(max_length=10, null=True, verbose_name='Псевдоним для системы'),
        ),
        migrations.AlterField(
            model_name='infopages',
            name='text',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='infopages',
            name='title',
            field=models.CharField(max_length=20, null=True, verbose_name='Заголовок'),
        ),
    ]
