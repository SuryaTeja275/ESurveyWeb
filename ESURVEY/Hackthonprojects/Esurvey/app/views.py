import re
from django import forms
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login as loginUser
from .models import *


# Create your views here.
def home(request):
    return render(request,"home.html")

def loginPage(request):
    return render(request,"login.html")


class SignInForm(forms.Form):
    loginEmail = forms.EmailField(label='Email')
    loginPassword = forms.CharField(label='Password', widget=forms.PasswordInput)


class SignUpForm(forms.Form):
    name = forms.CharField(label='Name')
    email = forms.EmailField(label='Email')
    pwd = forms.CharField(label='Password', widget=forms.PasswordInput)


def is_valid_password(password):
    if len(password) < 8:
        return False
    if not re.search(r'[a-z]', password):
        return False
    if not re.search(r'[A-Z]', password):
        return False
    if not re.search(r'\d', password):
        return False
    if not re.search(r'[@#$%^&+=]', password):
        return False
    return True


def signInUser(request):
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['loginEmail']
            password = form.cleaned_data['loginPassword']

            # Authenticate user
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('main')
            else:
                return render(request, 'signin.html', {'form': form, 'error': 'Invalid credentials'})
    else:
        form = SignInForm()
    return render(request, 'signin.html', {'form': form})

def signUpUser(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['pwd']

            # Create user
            user = UserModel.objects.create_user(name=name, email=email, password=password)
            user.save()
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def main(request):
    return render(request, "main.html")

def AU(request):
    return render(request, "AU.html")

def CU(request):
    return render(request, "CU.html")

from .models import Feedback  # Import your Feedback model here

def feedback(request):
    if request.method == "POST":
        name = request.POST.get('nm')
        mobile = request.POST.get('mb')
        address = request.POST.get('ad')
        survey_type = request.POST.get('st')
        customer_feedback = request.POST.get('cf')

        # Use a different name for the variable storing the model instance
        feedback_instance = Feedback.objects.create(
            name=name,
            mobile=mobile,
            address=address,
            survey_type=survey_type,
            customer_feedback=customer_feedback
        )
        feedback_instance.save()
        return redirect('main')  # Redirect to a success page after form submission
    return render(request, "feedback.html")


def TRS(request):
    if request.method == "POST":
        # Extracting data from the POST request
        question1 = request.POST.get('question1')
        question2 = request.POST.get('question2')
        question3 = request.POST.get('question3')
        question4 = request.POST.get('question4')
        question5 = request.POST.get('question5')
        question6 = request.POST.get('question6')
        question7 = request.POST.get('question7')
        question8 = request.POST.get('question8')

        # Creating the SurveyResponse object with extracted data
        survey_response = SurveyResponse.objects.create(
            question1=question1,
            question2=question2,
            question3=question3,
            question4=question4,
            question5=question5,
            question6=question6,
            question7=question7,
            question8=question8
        )

        # Optionally, you can save the object to the database
        survey_response.save()

        # Redirect to a success page after form submission
        return redirect('main')  # Assuming 'success' is a valid URL name

    # Render the template for GET requests
    return render(request, "TRS.html")

def ERS(request):
    if request.method == "POST":
        # Extracting data from the POST request
        question1 = request.POST.get('question1')
        question2 = request.POST.get('question2')
        question3 = request.POST.get('question3')
        question4 = request.POST.get('question4')
        question5 = request.POST.get('question5')
        question6 = request.POST.get('question6')
        question7 = request.POST.get('question7')
        question8 = request.POST.get('question8')

        # Creating the EducationalSurveyResponse object with extracted data
        survey_response = EducationalSurveyResponse.objects.create(
            question1=question1,
            question2=question2,
            question3=question3,
            question4=question4,
            question5=question5,
            question6=question6,
            question7=question7,
            question8=question8
        )

        # Optionally, you can save the object to the database
        survey_response.save()

        # Redirect to a success page after form submission
        return redirect('main')  # Assuming 'success' is a valid URL name

    # Render the template for GET requests
    return render(request, "ERS.html")

def GRS(request):
        if request.method == "POST":
            # Extracting data from the POST request
            hours_spent_per_week = request.POST.get('hours_spent_per_week')
            game_types = request.POST.getlist('game_type')
            importance_of_graphics = request.POST.get('importance_of_graphics')
            gaming_platforms = request.POST.getlist('platform')
            participated_in_esports = request.POST.get('participated_in_esports')
            learn_about_new_games = request.POST.get('learn_about_new_games')
            purchasing_decision_factors = request.POST.get('purchasing_decision_factors')
            communication_with_players = request.POST.get('communication_with_players')

            # Creating the GRS object with extracted data
            grs = GamingRS.objects.create(
                hours_spent_per_week=hours_spent_per_week,
                importance_of_graphics=importance_of_graphics,
                participated_in_esports=participated_in_esports,
                learn_about_new_games=learn_about_new_games,
                purchasing_decision_factors=purchasing_decision_factors,
                communication_with_players=communication_with_players
            )

            # Adding many-to-many relationships
            grs.game_types.add(*game_types)
            grs.gaming_platforms.add(*gaming_platforms)

            return redirect('main')  # Redirect to a success page after form submission

        return render(request, "GRS.html")

def NForm(request):
    if request.method == 'POST':
        favorite_genre = request.POST.get('question1')
        movies_watched_per_month = request.POST.get('question2')
        movie_genres_enjoyed = request.POST.get('genres')
        movie_watching_experience_rating = request.POST.get('question4')
        movie_platform_most_used = request.POST.get('question5')

        # Create a new FilmySurvey object and save it to the database
        FS=FilmySurvey.objects.create(
            favorite_genre=favorite_genre,
            movies_watched_per_month=movies_watched_per_month,
            movie_genres_enjoyed=movie_genres_enjoyed,
            movie_watching_experience_rating=movie_watching_experience_rating,
            movie_platform_most_used=movie_platform_most_used
        )

        return redirect('main')  # Redirect to a success page after form submission

    return render(request, 'NForm.html')
