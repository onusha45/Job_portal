from django import forms
from User_app.models import CustomUser

class Login(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta :
        model = CustomUser
        fields = ['email','password']

class UserSignup(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    
    class Meta :
        model = CustomUser
        fields = ['username','email','password','repassword','profile','resume']