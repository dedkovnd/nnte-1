# Generated by Django 3.0.4 on 2020-04-22 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0009_auto_20200419_1505'),
    ]

    operations = [
        migrations.AddField(
            model_name='section',
            name='sequence',
            field=models.SmallIntegerField(default=1, unique=True, verbose_name='Порядок следования'),
            preserve_default=False,
        ),
    ]
