from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import FoodItem
from .forms import FoodForm
from django.contrib.auth.decorators import permission_required
from django.views.generic import ListView


class ItemListView(ListView):
    model= FoodItem
    template_name = 'restaurant/index.html'

    def get_queryset(self):
        return FoodItem.objects.all().order_by('name')


#just admin
@permission_required('auth.view_user')
def updateItem(request, id):

    food = FoodItem.objects.get(id=id)    
    form = FoodForm(request.POST or None, request.FILES or None, instance=food)
    
    if request.POST and form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse("index"))

    return render(request, 'restaurant/form.html', {'form':form})


#just admin
@permission_required('auth.view_user')
def createItem(request):
    form = FoodForm(request.POST or None, request.FILES)
    if request.method == "POST":
       if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse("index"))
    
    
    return render(request, 'restaurant/form.html', {'form':form})


def description(request, id):
    food = FoodItem.objects.get(id=id)
    return render(request, 'restaurant/description.html', {'food':food})


#just admin
@permission_required('auth.view_user')
def deleteItem(request, id):
    FoodItem.objects.get(id=id).delete()
    return HttpResponseRedirect(reverse("index"))



