# Generated by Django 2.1.5 on 2019-02-12 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0010_auto_20190212_1435'),
    ]

    operations = [
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
