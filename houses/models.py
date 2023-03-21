from django.db import models
import uuid
from accounts.models import Account
from payments.models import Payment

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
    payments = models.ManyToManyField(Payment, blank=True)
