# Generated by Django 2.2.1 on 2019-06-14 14:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0013_auto_20190614_1435'),
    ]

    operations = [
        migrations.AddField(
            model_name='stad',
            name='vovo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Verenigingen', to='website.Verenigingen'),
        ),
    ]
