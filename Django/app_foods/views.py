from datetime import datetime
from django.shortcuts import render
from .models import Food

# Create your views here.


def foods(request):
    all_foods = Food.objects.order_by('-is_premium')
    context = {'foods': all_foods}
    return render(request, 'app_foods/foods.html', context)


def food(request, food_id):
    one_food = None
    #try:
    #    one_food = [f for f in all_foods if f['id'] == food_id][0]
    #except IndexError:
    #    print('empty')
    context = {'food': one_food}
    return render(request, 'app_foods/food.html', context)
