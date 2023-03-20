from django.urls import path
from . import views

urlpatterns = [
    path("show-hours", views.show_hours, name="show-hours"),
    path("delete-hour/<str:pk>", views.delete_hours, name="delete-hour"),
    path("add-hours", views.add_hours, name="add-hours"),
    path("set-work-hours", views.set_work_times, name="set-work-hours"),
    path("show-sum", views.calculate_hours, name="show-sum"),
]
