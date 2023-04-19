from django.urls import path
from . import views

urlpatterns = [
    path("show-houses/", views.show_houses, name="show-houses"),
    path("delete-house/<str:pk>", views.delete_house, name="delete-house"),
    path("add-house/", views.add_house, name="add-house"),
    path("edit-house/<str:pk>", views.edit_house, name="edit-house"),
    path("add-house-payment/", views.add_payment, name="add-house-payment"),
    path("add-payment-type/", views.add_payment_type, name="add-payment-type"),
    path("show-payments/", views.show_payments, name="show-payments"),
    path(
        "show-payment-types/",
        views.show_payment_types,
        name="show-payment-types",
    ),
    path(
        "edit-payment-types/<str:pk>",
        views.edit_payment_type,
        name="edit-payment-types",
    ),
    path(
        "delete-payment-type/<str:pk>",
        views.delete_payment_type,
        name="delete-payment-type",
    ),
]
