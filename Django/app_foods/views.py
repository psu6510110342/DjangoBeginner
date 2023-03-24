from django.shortcuts import render

all_food = [
    {'id': 1, 'title': 'Chocolate', 'price': 449, 'is_premium': True},
    {'id': 2, 'title': 'Red', 'price': 349, 'is_premium': False},
    {'id': 3, 'title': 'Bule', 'price': 349, 'is_premium': False}
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
