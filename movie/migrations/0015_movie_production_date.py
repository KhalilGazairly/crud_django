# Generated by Django 3.2.9 on 2021-11-08 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0014_alter_movie_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='production_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
