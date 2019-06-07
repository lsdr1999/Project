# Generated by Django 2.2.1 on 2019-06-07 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_auto_20190607_0957'),
    ]

    operations = [
        migrations.AlterField(
            model_name='verenigingen',
            name='contributie',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True),
        ),
        migrations.AlterField(
            model_name='verenigingen',
            name='leden',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='verenigingen',
            name='verhaal',
            field=models.URLField(blank=True, max_length=600, null=True),
        ),
    ]
