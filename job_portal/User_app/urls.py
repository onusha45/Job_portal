from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from User_app.views import *

urlpatterns =   [
     path('signup/', signup ,name='signup'),
     path('employer_signup', employer_signup, name="employer_signup"),
     path('jobseeker_signup', jobseeker_signup, name="jobseeker_signup"),
     path('login/',login,name='login'),
     path('jobseekerhome/', jobseekerhome ,name='jobseekerhome'),
     path('employerhome/', employerhome ,name='employerhome'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)