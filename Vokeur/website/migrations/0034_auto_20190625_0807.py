# Generated by Django 2.2.1 on 2019-06-25 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0033_auto_20190624_0922'),
    ]

    operations = [
        migrations.AlterField(
            model_name='verenigingen',
            name='verhaal',
            field=models.CharField(blank=True, max_length=1200, null=True),
        ),
    ]
