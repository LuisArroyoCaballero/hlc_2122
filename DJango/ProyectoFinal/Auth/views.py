from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.

def holaAuth(request):
    return HttpResponse("<h1>Esta es la página de Auth</h1>")

def login(request):
    return render(request, 'login.html')