# Generated by Django 3.0.4 on 2020-04-22 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0011_auto_20200422_0826'),
    ]

    operations = [
        migrations.AlterField(
            model_name='section',
            name='sequence',
            field=models.SmallIntegerField(unique=True, verbose_name='Порядок следования'),
        ),
    ]
