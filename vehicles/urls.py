from django.urls import path
from . import views

urlpatterns = [
    path("show-vehicles/", views.show_vehicles, name="show-vehicles"),
    path(
        "delete-vehicle/<str:pk>",
        views.delete_vehicle,
        name="delete-vehicle",
    ),
    path("edit-vehicle/<str:pk>", views.edit_vehicle, name="edit-vehicle"),
    path(
        "add-vehicle-payment/",
        views.add_payment,
        name="add-vehicle-payment",
    ),
    path("add-vehicle/", views.add_vehicle, name="add-vehicle"),
    path(
        "add-vehicle-payment-type/",
        views.add_payment_type,
        name="add-vehicle-payment-type",
    ),
    path(
        "show-payments-vehicle/",
        views.show_payments,
        name="show-vehicle-payments",
    ),
    path(
        "show-vehicle-payment-types/",
        views.show_payment_types,
        name="show-vehicle-payment-types",
    ),
    path(
        "edit-vehicle-payment-type/<str:pk>",
        views.edit_payment_type,
        name="edit-vehicle-payment-type",
    ),
    path(
        "delete-vehicle-payment-type/<str:pk>",
        views.delete_payment_type,
        name="delete-vehicle-payment-type",
    ),
    path(
        "show-payments-vehicle-license/<str:pk>",
        views.show_payments_from_vehicles,
        name="show-payments-vehicle",
    ),
    path(
        "show-payments-render/<str:pk>",
        views.show_payments_from_render,
        name="show-payments-vehicle-render",
    ),
    path(
        "show-payments-vehicle-payment-type/<str:pk>",
        views.show_payments_from_payment_type,
        name="show-payments-vehicle-payment-type",
    ),
]
