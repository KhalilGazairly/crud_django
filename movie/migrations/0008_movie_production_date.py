# Generated by Django 3.2.9 on 2021-11-07 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0007_remove_movie_production_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='production_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
