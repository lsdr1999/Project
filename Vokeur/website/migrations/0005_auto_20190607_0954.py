# Generated by Django 2.2.1 on 2019-06-07 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_auto_20190607_0948'),
    ]

    operations = [
        migrations.AddField(
            model_name='verenigingen',
            name='afbeelding',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='verenigingen',
            name='mail',
            field=models.EmailField(blank=True, max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='verenigingen',
            name='website',
            field=models.URLField(blank=True, max_length=64, null=True),
        ),
    ]
