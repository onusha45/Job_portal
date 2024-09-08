from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    profile = models.ImageField(upload_to='profile/', null=True, blank=True)
    resume = models.FileField(upload_to='resumes/', null=True, blank=True)
    isEmployeer = models.BooleanField(default=False)
    phone_no =models.IntegerField(null=True)
    address = models.CharField(max_length=50, null=True)
    company_name = models.CharField(max_length=200, null=True)


    def __str__(self):
          return self.username
