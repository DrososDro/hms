from django.db import models
from accounts.models import Account
import uuid

# Create your models here.


class Vehicles(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True)
    created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(Account, on_delete=models.CASCADE)

    licence_plate = models.CharField(max_length=20, unique=True)
    vin = models.CharField(max_length=200, unique=True, blank=True, null=True)
    brand = models.CharField(max_length=200, blank=True, null=True)
    model = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self) -> str:
        return self.licence_plate


class Payment(models.Model):
    CHOICE = [
        ("Payment", "Payment"),
        ("Income", "Income"),
    ]
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True)
    created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(
        Account,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="vehicle_owner",
    )

    vehicle = models.ForeignKey(Vehicles, on_delete=models.CASCADE)
    payment_type = models.ForeignKey("PaymentType", on_delete=models.CASCADE)
    payment = models.CharField(max_length=14, choices=CHOICE)

    render = models.ForeignKey(
        Account,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="vehicle_render",
    )
    file = models.FileField(blank=True, null=True)
    date_of_payment = models.DateField()
    price = models.FloatField()
    price_b = models.FloatField(blank=True, null=True)


class PaymentType(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True)
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name
