# Generated by Django 4.2.7 on 2023-11-22 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dave', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(unique=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
