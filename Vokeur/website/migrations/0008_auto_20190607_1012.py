# Generated by Django 2.2.1 on 2019-06-07 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0007_auto_20190607_1011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='verenigingen',
            name='verhaal',
            field=models.CharField(blank=True, max_length=600, null=True),
        ),
    ]