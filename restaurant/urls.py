from django.urls import path

from . import views

urlpatterns = [
    path("", views.ItemListView.as_view(), name="index"),
    path("item/form/", views.createItem, name="form"),
    path("item/delete/<int:id>/", views.deleteItem, name="delete"),
    path("item/form/<int:id>/", views.updateItem, name="form"),
    path("item/description/<int:id>/", views.description, name="description"),
]