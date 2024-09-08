from django.shortcuts import render,redirect
from django.contrib.auth import authenticate ,login as auth_login
from django.http import HttpResponse
from .forms import Login,UserSignup, EmployeerSignup
from .models import CustomUser

def signup(request):
    if request.method == "POST":
        form = UserSignup(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            
            password = form.cleaned_data.get('password')
            confirm_password = form.cleaned_data.get('repassword')
            is_Employeer = form.cleaned_data.get('isEmployeer')
            
            
            if password != confirm_password:
                form.add_error('repassword', 'Passwords do not match.')
            else:
                user.set_password(password)
                user.save()
                if(is_Employeer):
                    request.session["user_id"] = user.id
                    return redirect('employeer_signup')
                return redirect('login')
        else:
            print(form.errors)
            print(request.FILES)
            print(request.POST)
    else:
        form = UserSignup()
        
    context = {
        'form': form,
    }
    
    return render(request, 'signup.html', context)


def employeer_signup(request):
    if request.method == "POST":
        form = EmployeerSignup(request.POST)
        if form.is_valid():
            user_id = request.session.get('user_id')
            if not user_id:
                return redirect('signup')
            user = CustomUser.objects.get(pk=user_id)
            user.phone_no = form.cleaned_data['phone_no']
            user.address = form.cleaned_data['address']
            user.company_name = form.cleaned_data['company_name']
            user.save()

            del request.session['user_id']

            return redirect('login')
        else:
            print("Form errors:", form.errors)
    else:
        form = EmployeerSignup()
    
    return render(request, 'jobseekersignup.html', {"form": form})

        


def login(request):
    if request.method == 'POST':
        form = Login(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                print(user.isEmployeer)
                if user.isEmployeer:
                    print("emp")
                    return redirect('employeerhome')
                else:
                    print("jobseek")
                    return redirect('jobseekerhome') 
            else:
                form.add_error(None, 'Invalid email or password.')
        else:
            print("Not valid")
    else:
        form = Login()
        
    context = {
        'form': form
    }
    
    return render(request, 'login.html', context)



def jobseekerhome(request ):
   user = request.user
   context = {
       'user':user,
   }
   return render(request,'jobseekerhome.html',context)

def employeerhome(request):
    return render(request, "employeerhome.html")
