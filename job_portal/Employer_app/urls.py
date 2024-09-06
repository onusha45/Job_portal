from django.contrib import admin
from django.urls import path
from Employer_app.views import employersignup
urlpatterns = [
   path('employersignup/',employersignup,name= 'employersignup'),
] 