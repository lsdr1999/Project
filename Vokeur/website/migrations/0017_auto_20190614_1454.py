# Generated by Django 2.2.1 on 2019-06-14 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0016_auto_20190614_1452'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='verenigingen',
            name='stad',
        ),
        migrations.AlterField(
            model_name='stad',
            name='vovo',
            field=models.ManyToManyField(to='website.Verenigingen'),
        ),
    ]
