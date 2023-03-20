from django.db import models
import uuid
from accounts.models import Account

# Create your models here.


class WorkTime(models.Model):
    """
    here we set the time we have to be to work
    and what time we have to leave

    """

    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True
    )
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    owner = models.OneToOneField(Account, on_delete=models.CASCADE)
    work_hour_start = models.TimeField(null=True, blank=True)
    work_hour_end = models.TimeField(null=True, blank=True)


class WorkCalc(models.Model):
    """
    here we set the daily time of arrival and of leaving
    """

    VOTES = [
        ("0", "Normal"),
        ("1", "Weekend"),
        ("2", "Times off"),
        ("3", "Sick leave"),
        ("4", "Public holiday"),
    ]

    owner = models.ForeignKey(Account, on_delete=models.CASCADE)
    day = models.TextField(max_length=2, choices=VOTES, default="0")
    date = models.DateField()
    start_of_work = models.TimeField(null=True, blank=True)
    end_of_work = models.TimeField(null=True, blank=True)
    comment = models.CharField(max_length=200, null=True, blank=True)
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True
    )
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["date"]
