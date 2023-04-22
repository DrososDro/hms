# Generated by Django 4.2 on 2023-04-19 17:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("houses", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="payment",
            name="payment",
            field=models.CharField(
                choices=[("Payment", "Payment"), ("Income", "Income")], max_length=14
            ),
        ),
        migrations.AlterField(
            model_name="payment",
            name="payment_type",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="houses.paymenttype"
            ),
        ),
    ]