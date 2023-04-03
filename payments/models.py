from django.db import models
import uuid
from houses.models import House
from accounts.models import Account

# Create your models here.


class Payment(models.Model):
    CHOICE = [
        ("Payment", "Payment"),
        ("Income", "Income"),
    ]
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True)
    created = models.DateTimeField(auto_now_add=True)
    payment_type = models.CharField(max_length=14, choices=CHOICE)
    render = models.ForeignKey(Account, on_delete=models.CASCADE, blank=True)
    file = models.FileField(blank=True, null=True)
    date_of_payment = models.DateField()
    price = models.FloatField()
    price_b = models.FloatField()
    payment = models.ForeignKey("PaymentType", on_delete=models.CASCADE)
    house = models.ManyToManyField(House, blank=True)


class PaymentType(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True)
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name