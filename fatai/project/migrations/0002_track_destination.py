# Generated by Django 3.1.7 on 2021-03-05 01:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='track',
            name='destination',
            field=models.CharField(default='Your Location', max_length=100),
        ),
    ]