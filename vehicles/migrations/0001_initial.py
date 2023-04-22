# Generated by Django 4.2 on 2023-04-22 09:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="PaymentType",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("name", models.CharField(max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="Vehicles",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("licence_plate", models.CharField(max_length=20, unique=True)),
                (
                    "vin",
                    models.CharField(
                        blank=True, max_length=200, null=True, unique=True
                    ),
                ),
                ("brand", models.CharField(blank=True, max_length=200, null=True)),
                ("model", models.CharField(blank=True, max_length=200, null=True)),
                (
                    "owner",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Payment",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True)),
                (
                    "payment",
                    models.CharField(
                        choices=[("Payment", "Payment"), ("Income", "Income")],
                        max_length=14,
                    ),
                ),
                ("file", models.FileField(blank=True, null=True, upload_to="")),
                ("date_of_payment", models.DateField()),
                ("price", models.FloatField()),
                ("price_b", models.FloatField(blank=True, null=True)),
                (
                    "owner",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="vehicle_owner",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "payment_type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="vehicles.paymenttype",
                    ),
                ),
                (
                    "render",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="vehicle_render",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "vehicle",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="vehicles.vehicles",
                    ),
                ),
            ],
        ),
    ]