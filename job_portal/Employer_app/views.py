from django.shortcuts import render,redirect
# from .forms import EmployerSignup
# Create your views here.
def employersignup(request):
     if request.method == "POST":

       form = EmployerSignup(request.POST,request)
       if form.is_valid():
        employer = form.save(commit=False)
        password = request.POST.get('password')
        employer.save()
        return redirect('login')
       else:
            print(form.errors)
      
     else:
       form = EmployerSignup()
     context = {
        'form':form
    }
     return render(request,'employersignup.html',context)
def employerhome(request):
   return render(request,'employerhome.html')