from django import forms
from User_app.models import CustomUser

class Login(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta :
        model = CustomUser
        fields = ['email','password']

class UserSignup(forms.ModelForm):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    repassword = forms.CharField(widget=forms.PasswordInput)
    class Meta :
        model = CustomUser
        fields = ['first_name','last_name','email','password','repassword','profile','resume']