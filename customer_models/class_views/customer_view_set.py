from django_rest_framework.pagination import StandardResultsSetPagination
from rest_framework import viewsets, permissions
from rest_framework_simplejwt.authentication import JWTAuthentication

from customer_models.class_models.customer import Customer
from customer_models.class_serializers.customer_serializers import CustomerSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    pagination_class = StandardResultsSetPagination
    serializer_class = CustomerSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)  # IsAuthenticated, IsAuthenticatedOrReadOnly
    authentication_classes = [JWTAuthentication, ]
