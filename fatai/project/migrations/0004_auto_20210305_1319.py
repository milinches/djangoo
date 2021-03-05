# Generated by Django 3.1.7 on 2021-03-05 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_auto_20210305_0241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='track',
            name='date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='track',
            name='status',
            field=models.IntegerField(choices=[(0, 'NIL'), (1, 'Delivered'), (3, 'On the way')], default=1),
        ),
    ]