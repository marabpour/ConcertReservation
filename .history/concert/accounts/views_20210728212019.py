from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def loginView(request):
    return render(request,"accounts/login.html",{})