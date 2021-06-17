from django_rest_framework.pagination import StandardResultsSetPagination
from rest_framework import viewsets

from customer_models.class_models.customer_address import CustomerAddress
from customer_models.class_serializers.customer_address_serializers import CustomerAddressSerializer


class CustomerAddressViewSet(viewsets.ModelViewSet):
    queryset = CustomerAddress.objects.all()
    pagination_class = StandardResultsSetPagination
    serializer_class = CustomerAddressSerializer
