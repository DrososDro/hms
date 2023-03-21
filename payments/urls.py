from django.urls import path
from . import views


urlpatterns = [
    path("add-payment-type/", views.add_payment_type, name="add-payment-type"),
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
