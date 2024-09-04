from django import forms
from .models import EmployerSignup

class EmployerSignup(forms.ModelForm):
    class Meta:
        model = EmployerSignup
        fields = ['Company_name','Email','Password','Confirm_password','Phone_no','Address']

