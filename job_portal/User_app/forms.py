from django import forms
from User_app.models import CustomUser

class Login(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)

class UserSignup(forms.ModelForm):
    repassword = forms.CharField(widget=forms.PasswordInput)
    class Meta :
        model = CustomUser
        fields = ['username','first_name','last_name','email','password', 'repassword','profile','resume', 'isEmployeer']

class EmployeerSignup(forms.ModelForm):
    class Meta :
        model = CustomUser
        fields = ['phone_no', 'address', 'company_name']