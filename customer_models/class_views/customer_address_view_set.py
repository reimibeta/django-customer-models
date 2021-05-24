from rest_framework import viewsets
from rest_framework_utils.pagination import StandardResultsSetPagination

from customer_models.class_models.customer_address import CustomerAddress
from customer_models.class_serializers.customer_address_serializers import CustomerAddressSerializer


class CustomerAddressViewSet(viewsets.ModelViewSet):
    queryset = CustomerAddress.objects.all()
    pagination_class = StandardResultsSetPagination
    serializer_class = CustomerAddressSerializer
