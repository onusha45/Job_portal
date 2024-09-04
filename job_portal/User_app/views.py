from django.shortcuts import render
from django.http import HttpResponse
from .forms import Login,UserSignup

def jobseekersignup(request):
    form = UserSignup()
    context ={
        'form':form,
    }
    return render(request,'jobseekersignup.html',context)
def login (request):
    form = Login()
    context = {
        'form' : form
    }
    return render(request,'login.html',context)