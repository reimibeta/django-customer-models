from django.db import models

from customer_models.class_models.customer import Customer


class CustomerPhone(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='customer_phones')
    region = models.CharField(max_length=10, blank=True, null=True, editable=False)
    country_code = models.CharField(max_length=100, blank=True, null=True, editable=False)
    national = models.CharField(max_length=100, blank=True, null=True, editable=False)
    national_number = models.CharField(max_length=100, blank=True, null=True, editable=False)
    international = models.CharField(max_length=100, blank=True, null=True, editable=False)
    international_standard = models.CharField(max_length=100, blank=True, null=True, editable=False)
    type = models.CharField(max_length=100, blank=True, null=True, editable=False)
    phone = models.CharField(max_length=255, blank=True, null=True, unique=True)

    def __str__(self):
        return self.phone
