from datetime import datetime
from django.shortcuts import render

all_food = [
    {
        'id': 1,
        'title': 'Chocolate',
        'price': 1449,
        'is_premium': True,
        'promosion_end_at': datetime(2022, 2, 28)
    },
    {
        'id': 2,
        'title': 'Red',
        'price': 1349,
        'is_premium': False,
        'promosion_end_at': datetime(2022, 2, 15)
    },
    {
        'id': 3,
        'title': 'Bule',
        'price': 1349,
        'is_premium': False,
        'promosion_end_at': datetime(2022, 2, 15)
    }
]

# Create your views here.


def foods(request):
    context = {'foods': all_food}
    return render(request, 'app_foods/foods.html', context)


def food(request, food_id):
    one_food = None
    try:
        one_food = [f for f in all_food if f['id'] == food_id][0]
    except IndexError:
        print('empty')
    context = {'food': one_food}
    return render(request, 'app_foods/food.html', context)
