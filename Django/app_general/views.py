from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('<h1>home</h1>')

def about(request):
    return HttpResponse('<h1>about</h1>')
