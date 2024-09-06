from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from User_app.views import *

urlpatterns =   [
     path('jobseekersignup/', jobseekersignup ,name='jobseekersignup'),
     path('login/',login,name='login'),
     path('userhome/',userhome ,name='userhome'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)