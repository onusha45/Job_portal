from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from User_app.views import *

urlpatterns =   [
     path('signup/', signup ,name='signup'),
     path('employeer_signup', employeer_signup, name="employeer_signup"),
     path('login/',login,name='login'),
     path('jobseekerhome/', jobseekerhome ,name='jobseekerhome'),
     path('employeerhome/', employeerhome ,name='employeerhome'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)