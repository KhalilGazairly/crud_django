# Generated by Django 3.2.9 on 2021-11-07 20:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0008_movie_production_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='production_date',
        ),
    ]
