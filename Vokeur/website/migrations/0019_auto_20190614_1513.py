# Generated by Django 2.2.1 on 2019-06-14 15:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0018_stad_vivi'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stad',
            old_name='vovo',
            new_name='ver',
        ),
        migrations.RemoveField(
            model_name='stad',
            name='vivi',
        ),
    ]
