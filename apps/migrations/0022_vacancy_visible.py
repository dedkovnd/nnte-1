# Generated by Django 3.0.4 on 2020-04-25 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0021_auto_20200425_1121'),
    ]

    operations = [
        migrations.AddField(
            model_name='vacancy',
            name='visible',
            field=models.BooleanField(default=True, verbose_name='Видимый'),
        ),
    ]
