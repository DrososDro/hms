from django.urls import path
from . import views

urlpatterns = [
    path("show-houses/", views.show_houses, name="show-houses"),
    path("delete-house/<str:pk>", views.delete_house, name="delete-house"),
    path("add-house/", views.add_house, name="add-house"),
    path("edit-house/<str:pk>", views.edit_house, name="edit-house"),
    path("add-house-payment/", views.add_payment, name="add-house-payment"),
]
