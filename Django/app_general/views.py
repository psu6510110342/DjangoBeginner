from django.shortcuts import render
from app_foods.models import Food
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Subscription

# Create your views here.
def home(request):
    return render(request, 'app_general/home.html')

def about(request):
    return render(request, 'app_general/about.html')

def subscription(request):
    if request.POST:
        name = request.POST.get('name')
        email = request.POST.get('email')
        food_ids = request.POST.getlist('food_ids[]')
        new_sub = Subscription()
        new_sub.name = name
        print(name)
        print(email)
        print(food_ids)
        return HttpResponseRedirect(reverse('sub_ty'))
    all_foods = Food.objects.order_by('-is_premium')
    context = {'foods': all_foods}
    return render(request, 'app_general/subscription_from.html', context )

def sub_ty(request):
    return render(request, 'app_general/sub_ty.html')