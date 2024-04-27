# Generated by Django 4.1.13 on 2024-04-26 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_usermodel_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='SurveyResponse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question1', models.CharField(max_length=50)),
                ('question2', models.CharField(max_length=100)),
                ('question3', models.CharField(max_length=100)),
                ('question4', models.CharField(max_length=100)),
                ('question5', models.CharField(max_length=20)),
                ('question6', models.CharField(max_length=100)),
                ('question7', models.TextField()),
                ('question8', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='email',
            field=models.EmailField(max_length=33),
        ),
    ]