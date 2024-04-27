from django.urls import *
from .views import *

urlpatterns=[
    path('',home,name="home"),
    path('login',loginPage,name="login"),
    path('main', main, name='main'),
    path('AU',AU,name="AU"),
    path('signInUser',signInUser,name='signInUser'),
    path('signUpUser',signUpUser,name='signUpUser'),
    path('CU',CU,name="CU"),
    path('feedback',feedback,name="feedback"),
    path('TRS', TRS, name="TRS"),
    path('ERS', ERS, name="ERS"),
    path('GRS', GRS, name="GRS"),
    path('NForm', NForm, name="NForm"),

]