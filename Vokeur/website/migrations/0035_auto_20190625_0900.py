# Generated by Django 2.2.1 on 2019-06-25 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0034_auto_20190625_0807'),
    ]

    operations = [
        migrations.AlterField(
            model_name='verenigingen',
            name='adres',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
