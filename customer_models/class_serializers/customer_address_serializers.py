from rest_flex_fields import FlexFieldsModelSerializer

# product size serializer
from customer_models.class_models.customer_address import CustomerAddress


class CustomerAddressSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = CustomerAddress
        fields = [
            'id',
            'url',
            'customer',
            'address',
            'map',
            'city',
            'country'
        ]
        # expandable_fields = {'customer': CustomerSerializer}
