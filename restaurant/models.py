from pyexpat import model
from django.db import models
from django.utils.html import mark_safe

class FoodItem(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='restaurant_images', height_field=None, width_field=None, max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=500)

    def __str__(self):
        #return '{} and {}'.format(self.name, self.description)
        return self.name

    def image_tag(self):
        return mark_safe('<img src="/directory/%s" width="150" height="150" />' % (self.image))

    image_tag.short_description = 'Image'

    