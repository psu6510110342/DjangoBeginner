from django.shortcuts import render
from app_foods.models import Food
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Subscription
from .forms import SubForm

# Create your views here.
def home(request):
    return render(request, 'app_general/home.html')

def about(request):
    return render(request, 'app_general/about.html')

def subscription(request):
    if request.method == 'POST':
        form = SubForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_sub = Subscription()
            new_sub.name = data['name']
            new_sub.email = data['email']
            new_sub.save()
            new_sub.food_set.set(data['food_set'])
            return HttpResponseRedirect(reverse('sub_ty'))
    else:
        form = SubForm()
    context = {'form': form}
    return render(request, 'app_general/subscription_from.html', context )

def sub_ty(request):
    return render(request, 'app_general/sub_ty.html')