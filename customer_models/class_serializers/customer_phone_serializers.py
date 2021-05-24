from rest_flex_fields import FlexFieldsModelSerializer
from rest_framework import serializers

# customer hyper serializer
from customer_models.class_models.customer_phone import CustomerPhone


class CustomerPhoneSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = CustomerPhone
        fields = ['id', 'url', 'customer', 'phone']
        # expandable_fields = {'customer': CustomerSerializer}
