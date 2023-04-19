from django.contrib import admin
from .models import House, Payment, PaymentType

# Register your models here.


admin.site.register(House)
admin.site.register(Payment)
admin.site.register(PaymentType)
