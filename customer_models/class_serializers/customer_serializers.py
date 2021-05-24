from rest_flex_fields import FlexFieldsModelSerializer
from rest_framework import serializers

# customer hyper serializer
from customer_models.class_models.customer import Customer
from customer_models.class_serializers.customer_address_serializers import CustomerAddressSerializer
from customer_models.class_serializers.customer_phone_serializers import CustomerPhoneSerializer


class CustomerSerializer(FlexFieldsModelSerializer):
    customer_phones = serializers.PrimaryKeyRelatedField(read_only=True, many=True)
    customer_address = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Customer
        fields = [
            'id',
            'url',
            'name',
            'created_date',
            'status',
            'customer_phones',
            'customer_address'
        ]
        expandable_fields = {
            'customer_phones': (CustomerPhoneSerializer, {'many': True}),
            'customer_address': CustomerAddressSerializer,
        }
