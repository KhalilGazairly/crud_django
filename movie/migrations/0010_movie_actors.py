# Generated by Django 3.2.9 on 2021-11-07 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0009_remove_movie_production_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='actors',
            field=models.ManyToManyField(to='movie.Actor'),
        ),
    ]
