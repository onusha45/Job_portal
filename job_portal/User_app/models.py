from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class CustomUser(AbstractUser):
    repassword = models.CharField(max_length=128, null=True, blank=True)
    profile = models.ImageField(upload_to='profile/', null=True, blank=True)
    resume = models.FileField(upload_to='resumes/', null=True, blank=True)

    def __str__(self):
          return self.first_name
