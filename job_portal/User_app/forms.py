from django import forms
from .models import CustomUser

class Login(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta :
        model = CustomUser
        fields = ['email','password']

class UserSignup(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    
    class Meta :
        model = CustomUser
        fields = ['first_name','last_name','email','password','repassword','profile','resume']