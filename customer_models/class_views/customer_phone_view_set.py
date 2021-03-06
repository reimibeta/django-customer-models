from django_rest_framework.pagination import StandardResultsSetPagination
from rest_framework import viewsets

from customer_models.class_models.customer_phone import CustomerPhone
from customer_models.class_serializers.customer_phone_serializers import CustomerPhoneSerializer


class CustomerPhoneViewSet(viewsets.ModelViewSet):
    queryset = CustomerPhone.objects.all()
    pagination_class = StandardResultsSetPagination
    serializer_class = CustomerPhoneSerializer
