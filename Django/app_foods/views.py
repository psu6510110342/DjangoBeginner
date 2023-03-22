from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.
def foods(request):
    return HttpResponse('<h1>homefoods</h1>')
