# Generated by Django 2.0.3 on 2018-05-17 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0002_auto_20180517_0053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='infopages',
            name='alias',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='infopages',
            name='title',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
