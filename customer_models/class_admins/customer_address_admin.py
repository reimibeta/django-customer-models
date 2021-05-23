from django.contrib import admin
from django_admin_listfilter_dropdown.filters import DropdownFilter

from customer_models.class_models.customer_address import CustomerAddress


class CustomerAddressAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer', 'address', 'map', 'city', 'country']
    list_display_links = ['customer', ]
    list_per_page = 25
    list_filter = (
        # for ordinary fields
        ('customer__name', DropdownFilter),
        # for choice fields
        # ('a_choicefield', ChoiceDropdownFilter),
        # for related fields
        # ('user', RelatedDropdownFilter),
    )


admin.site.register(CustomerAddress, CustomerAddressAdmin)


class CustomerAddressAdminInline(admin.TabularInline):
    model = CustomerAddress
    extra = 0
