# Generated by Django 2.2.1 on 2019-06-14 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0014_stad_vovo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stad',
            name='vovo',
        ),
        migrations.AddField(
            model_name='stad',
            name='vovo',
            field=models.ManyToManyField(blank=True, null=True, related_name='Verenigingen', to='website.Verenigingen'),
        ),
    ]
