from django.contrib import admin
from .models import Vehicles, Payment, PaymentType

# Register your models here.


admin.site.register(Vehicles)
admin.site.register(Payment)
admin.site.register(PaymentType)
