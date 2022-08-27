from django.contrib import admin
from .models import FoodItem

fields = ['image_tag']
readonly_fields = ['image_tag']

admin.site.register(FoodItem)
