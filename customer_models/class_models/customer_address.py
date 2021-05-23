from django.db import models

from customer_models.class_models.customer import Customer


class CustomerAddress(models.Model):
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE, related_name='customer_address')
    address = models.CharField(max_length=255, blank=True, null=True)
    map = models.CharField(max_length=200, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return "{}".format(self.address)
