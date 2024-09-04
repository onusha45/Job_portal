from django.shortcuts import render
from .forms import EmployerSignup
# Create your views here.
def employersignup(request):
    form = EmployerSignup()
    context = {
        'form':form
    }
    return render(request,'employersignup.html',context)