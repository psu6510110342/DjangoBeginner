from django import forms
from app_foods.models import Food
from .models import Subscription


class FoodMultipleChoiceField(forms.ModelMultipleChoiceField):
    def label_from_instance(self, obj):
        return obj.title


class SubForm(forms.Form):
    name = forms.CharField(max_length=60, required=True, label='name')
    email = forms.EmailField(max_length=60, required=True, label='email')
    

class SubModelForm(forms.ModelForm):
    food_set = FoodMultipleChoiceField(
        queryset=Food.objects.order_by('-is_premium'),
        required=True,
        label='menu',
        widget=forms.CheckboxSelectMultiple)
    accepted = forms.BooleanField(required=True, label='accept')
    
    class Meta:
        model = Subscription
        fields = ['name', 'email', 'food_set', 'accepted']
        lables = {
            'name': 'name',
            'email': 'email',
            'food_set': 'menu',       
        }
