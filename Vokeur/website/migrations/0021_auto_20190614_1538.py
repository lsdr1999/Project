# Generated by Django 2.2.1 on 2019-06-14 15:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0020_auto_20190614_1525'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stad',
            name='vivi',
        ),
        migrations.AddField(
            model_name='verenigingen',
            name='stad',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='website.Stad'),
            preserve_default=False,
        ),
    ]
