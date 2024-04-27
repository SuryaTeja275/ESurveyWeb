from django.db import models

# Create your models here.
class UserModel(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=33)
    password = models.CharField(max_length=10)
    class Meta:
        db_table = "site_users"
class SurveyResponse(models.Model):
    question1 = models.CharField(max_length=50)
    question2 = models.CharField(max_length=100)
    question3 = models.CharField(max_length=100)
    question4 = models.CharField(max_length=100)
    question5 = models.CharField(max_length=20)
    question6 = models.CharField(max_length=100)
    question7 = models.TextField()
    question8 = models.CharField(max_length=100)

    def __str__(self):
        return f"Survey Response {self.id}"

class EducationalSurveyResponse(models.Model):
    SATISFACTION_CHOICES = [
        ('very_satisfied', 'Very Satisfied'),
        ('satisfied', 'Satisfied'),
        ('neutral', 'Neutral'),
        ('dissatisfied', 'Dissatisfied'),
        ('very_dissatisfied', 'Very Dissatisfied'),
    ]

    EFFECTIVENESS_CHOICES = [
        ('very_effective', 'Very Effective'),
        ('effective', 'Effective'),
        ('neutral', 'Neutral'),
        ('ineffective', 'Ineffective'),
        ('very_ineffective', 'Very Ineffective'),
    ]

    SATISFACTION_CHOICES_SHORT = [
        ('very_satisfied', 'Very Satisfied'),
        ('satisfied', 'Satisfied'),
        ('neutral', 'Neutral'),
        ('dissatisfied', 'Dissatisfied'),
        ('very_dissatisfied', 'Very Dissatisfied'),
    ]

    SATISFACTION_CHOICES_TEACHER = [
        ('very_satisfied', 'Very Satisfied'),
        ('satisfied', 'Satisfied'),
        ('neutral', 'Neutral'),
        ('dissatisfied', 'Dissatisfied'),
        ('very_dissatisfied', 'Very Dissatisfied'),
    ]

    question1 = models.CharField(max_length=20, choices=SATISFACTION_CHOICES)
    question2 = models.TextField()
    question3 = models.CharField(max_length=20, choices=EFFECTIVENESS_CHOICES)
    question4 = models.CharField(max_length=100)
    question5 = models.CharField(max_length=10, choices=[('yes', 'Yes'), ('no', 'No'), ('unsure', 'Unsure')])
    question6 = models.CharField(max_length=100)
    question7 = models.TextField()
    question8 = models.CharField(max_length=20, choices=SATISFACTION_CHOICES_TEACHER)

    def __str__(self):
        return f"Educational Survey Response {self.id}"

class Feedback(models.Model):
    name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=10)
    address = models.TextField()
    SURVEY_TYPES = [
        ('product_feedback', 'Research Survey'),
        ('customer_service', 'Educational Survey'),
        ('website_experience', 'Gaming Survey'),
        ('filmy_survey', 'Filmy Survey'),
    ]
    survey_type = models.CharField(max_length=20, choices=SURVEY_TYPES)
    customer_feedback = models.TextField()

# Choices for certain fields
IMPORTANCE_CHOICES = [
    ('very_important', 'Very Important'),
    ('important', 'Important'),
    ('neutral', 'Neutral'),
    ('not_important', 'Not Important'),
    ('not_at_all_important', 'Not At All Important'),
]

YES_NO_CHOICES = [
    ('yes', 'Yes'),
    ('no', 'No'),
]

COMMUNICATION_CHOICES = [
    ('always', 'Always'),
    ('often', 'Often'),
    ('sometimes', 'Sometimes'),
    ('rarely', 'Rarely'),
    ('never', 'Never'),
]

class GameType(models.Model):
    name = models.CharField(max_length=50)

class GamingPlatform(models.Model):
    name = models.CharField(max_length=50)
class GamingRS(models.Model):
    hours_spent_per_week = models.PositiveIntegerField()
    game_types = models.ManyToManyField('GameType', related_name='surveys')
    importance_of_graphics = models.CharField(max_length=20, choices=IMPORTANCE_CHOICES)
    gaming_platforms = models.ManyToManyField('GamingPlatform', related_name='surveys')
    participated_in_esports = models.CharField(max_length=3, choices=YES_NO_CHOICES)
    learn_about_new_games = models.CharField(max_length=100)
    purchasing_decision_factors = models.TextField()
    communication_with_players = models.CharField(max_length=10, choices=COMMUNICATION_CHOICES)

class FilmySurvey(models.Model):
    favorite_genre = models.CharField(max_length=100)
    movies_watched_per_month = models.PositiveIntegerField()
    movie_genres_enjoyed = models.CharField(max_length=100)
    movie_watching_experience_rating = models.IntegerField(choices=[(i, i) for i in range(1, 11)])
    movie_platform_most_used = models.CharField(max_length=100)