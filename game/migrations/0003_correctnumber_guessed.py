# Generated by Django 4.2.11 on 2024-05-15 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0002_correctnumber_maxnumber'),
    ]

    operations = [
        migrations.AddField(
            model_name='correctnumber',
            name='guessed',
            field=models.BooleanField(default=False),
        ),
    ]
