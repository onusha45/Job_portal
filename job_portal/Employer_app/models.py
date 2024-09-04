from django.db import models

# Create your models here.
class EmployerSignup(models.Model):
    Company_name = models.CharField(max_length=200)
    Email = models.EmailField(max_length=50,null=True,blank=True)
    Password = models.CharField(max_length=16,null=True,blank=True)
    Confirm_password = models.CharField(max_length=16,null=True,blank=True)
    Phone_no =models.IntegerField()
    Address = models.CharField(max_length=50)
    
    


    def __str__(self) :
        return self.Company_name