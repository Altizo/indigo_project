# Generated by Django 2.0.3 on 2018-05-28 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_auto_20180528_2333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='preview',
            name='full_size',
            field=models.ImageField(default='default', upload_to='portfolio/static/img/full_size/', verbose_name='Оригинал'),
        ),
        migrations.AlterField(
            model_name='preview',
            name='thumbs',
            field=models.ImageField(default='default', upload_to='portfolio/static/img/thumbs/', verbose_name='Превью 250х250px'),
        ),
    ]
