# Generated by Django 4.1.13 on 2024-04-27 00:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_gametype_gamingplatform_gamingrs'),
    ]

    operations = [
        migrations.DeleteModel(
            name='SurveyResponse',
        ),
    ]