# Generated by Django 4.1.7 on 2023-03-20 17:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("work_hours", "0003_alter_workcalc_options"),
    ]

    operations = [
        migrations.AlterField(
            model_name="worktime",
            name="owner",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
    ]