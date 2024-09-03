from django.shortcuts import render
from django.http import HttpResponse


def jobseekersignup(request):
    return render(request,'jobseekersignup.html')