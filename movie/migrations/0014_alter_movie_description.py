# Generated by Django 3.2.9 on 2021-11-08 00:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0013_auto_20211107_2327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='description',
            field=models.TextField(verbose_name='Movie Description'),
        ),
    ]
