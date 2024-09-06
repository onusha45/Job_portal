from django.contrib import admin
from django.urls import path
from Employer_app.views import *
urlpatterns = [
   path('employersignup/',employersignup,name= 'employersignup'),
   path('employerhome/', employerhome ,name= 'employerhome'),
] 