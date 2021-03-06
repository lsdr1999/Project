# Generated by Django 2.2.1 on 2019-06-07 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_auto_20190607_0954'),
    ]

    operations = [
        migrations.RenameField(
            model_name='verenigingen',
            old_name='locatie',
            new_name='adres',
        ),
        migrations.AddField(
            model_name='verenigingen',
            name='stad',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='verenigingen',
            name='verhaal',
            field=models.URLField(blank=True, max_length=500, null=True),
        ),
    ]
