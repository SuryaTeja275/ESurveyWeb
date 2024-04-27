# Generated by Django 4.1.13 on 2024-04-26 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_feedback'),
    ]

    operations = [
        migrations.CreateModel(
            name='GameType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='GamingPlatform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='GamingRS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hours_spent_per_week', models.PositiveIntegerField()),
                ('importance_of_graphics', models.CharField(choices=[('very_important', 'Very Important'), ('important', 'Important'), ('neutral', 'Neutral'), ('not_important', 'Not Important'), ('not_at_all_important', 'Not At All Important')], max_length=20)),
                ('participated_in_esports', models.CharField(choices=[('yes', 'Yes'), ('no', 'No')], max_length=3)),
                ('learn_about_new_games', models.CharField(max_length=100)),
                ('purchasing_decision_factors', models.TextField()),
                ('communication_with_players', models.CharField(choices=[('always', 'Always'), ('often', 'Often'), ('sometimes', 'Sometimes'), ('rarely', 'Rarely'), ('never', 'Never')], max_length=10)),
                ('game_types', models.ManyToManyField(related_name='surveys', to='app.gametype')),
                ('gaming_platforms', models.ManyToManyField(related_name='surveys', to='app.gamingplatform')),
            ],
        ),
    ]
