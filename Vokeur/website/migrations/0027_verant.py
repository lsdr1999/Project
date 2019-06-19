# Generated by Django 2.2.1 on 2019-06-19 14:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0026_letter_woorden'),
    ]

    operations = [
        migrations.CreateModel(
            name='Verant',
            fields=[
                ('id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='website.Vragen')),
                ('antwoord', models.CharField(blank=True, max_length=14, null=True)),
                ('vereniging', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='verant', to='website.Verenigingen')),
            ],
        ),
    ]
