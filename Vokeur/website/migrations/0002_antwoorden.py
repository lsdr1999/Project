# Generated by Django 2.2.1 on 2019-06-06 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Antwoorden',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('antwoorden', models.CharField(choices=[('Eens', 'Eens'), ('Oneens', 'Oneens'), ('Geen van beide', 'Geen van beide')], default=None, max_length=15)),
            ],
        ),
    ]