# Generated by Django 2.0.3 on 2018-05-16 21:53

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='infopages',
            name='alias',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='infopages',
            name='title',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='infopages',
            name='text',
            field=ckeditor.fields.RichTextField(null=True),
        ),
    ]