# Generated by Django 3.1.7 on 2021-03-05 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0005_track_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='track',
            name='slug',
            field=models.SlugField(max_length=100),
        ),
    ]
