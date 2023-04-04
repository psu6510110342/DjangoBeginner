from django import forms
from app_foods.models import Food
class SubForm(forms.Form):
    name = forms.CharField(max_length=60, required=True, label='name')
    email = forms.EmailField(max_length=60, required=True, label='email')
    food_set = forms.ModelMultipleChoiceField(
        queryset=Food.objects.order_by('-is_premium'),
        required=True, 
        label='menu',
        widget=forms.CheckboxSelectMultiple)
    accepted = forms.BooleanField(required=True, label='accept')