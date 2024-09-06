from django.shortcuts import render,redirect
from django.contrib.auth import authenticate ,login as auth_login
from django.http import HttpResponse
from .forms import Login,UserSignup
from .models import CustomUser

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


def login(request):
       if request.method == 'POST':
          form = Login(request.POST)
          if form.is_valid():
              email = request.POST['email']
              password = request.POST['password']
              # Authenticate using the email field
              try:
                  username = CustomUser.objects.get(email=email).username
                  user = authenticate(request, username=username, password=password)
                  if user is not None:
                      Login(request, user)
                      return redirect('userhome')  
                  else:
                      form.add_error(None, "Invalid email or password")
              except CustomUser.DoesNotExist:
                  form.add_error(None, "Invalid email or password")
       else:
          form = Login()
  
       context = {
        'form': form
                }
       return render(request, 'login.html', context)
def userhome(request):
   return render(request,'userhome.html')