from enum import Enum

from datetime_utils.date_time import DateTime
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class CustomerPriority(Enum):
    NORMAL = "normal"
    REGULAR = "regular"
    VIP = "vip"
    TOP = "top"

    @classmethod
    def choices(cls):
        # print(tuple((i.name, i.value) for i in cls))
        return tuple((i.name, i.value) for i in cls)


class Customer(models.Model):
    name = models.CharField(max_length=255)
    priority = models.CharField(max_length=60, choices=CustomerPriority.choices(), blank=True, null=True)
    created_date = models.DateField(default=DateTime(config='date').now())
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name
