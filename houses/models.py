from django.db import models
import uuid
from accounts.models import Account

# Create your models here.


class House(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True)
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    post_ofice = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    number = models.CharField(max_length=100)
    owner = models.ForeignKey(Account, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name


class Payment(models.Model):
    CHOICE = [
        ("Payment", "Payment"),
        ("Income", "Income"),
    ]
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True)
    created = models.DateTimeField(auto_now_add=True)

    house = models.ForeignKey(House, on_delete=models.CASCADE)
    payment_type = models.ForeignKey("PaymentType", on_delete=models.CASCADE)
    render = models.ForeignKey(Account, on_delete=models.CASCADE, blank=True)
    payment = models.CharField(max_length=14, choices=CHOICE)
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
