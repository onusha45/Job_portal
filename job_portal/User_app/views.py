from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import Login,UserSignup

def jobseekersignup(request):
    if request.method == "POST":

     form = UserSignup(request.POST,request.FILES)
     if form.is_valid():
        user = form.save(commit=False)
        password = request.POST.get('password')
        user.set_password(password)
        user.save()
        return redirect('login')
     else:
            print(form.errors)
            print(request.FILES)
            print(request.POST)
    
    else:
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