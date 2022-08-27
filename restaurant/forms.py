from django import forms
from django.forms import ModelForm
from .models import FoodItem

class FoodForm(ModelForm):
    class Meta:
        model = FoodItem
        fields = ['name','image', 'price', 'description']
        
    def clean(self):
        cleaned_data = super(FoodForm, self).clean()
        password = cleaned_data.get('password')
        confirm_pass = cleaned_data.get('confirmpass')

        if password != confirm_pass:
            raise forms.ValidationError(
                "Password and confirm password does not match"
            )
        print(cleaned_data)
        return cleaned_data