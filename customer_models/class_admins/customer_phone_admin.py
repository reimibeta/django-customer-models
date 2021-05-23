from django.contrib import admin
from django_admin_listfilter_dropdown.filters import DropdownFilter, RelatedDropdownFilter

from customer_models.class_models.customer_phone import CustomerPhone


class CustomerPhoneAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer', 'phone']
    list_display_links = ['customer', ]
    list_per_page = 25

    list_filter = (
        # for ordinary fields
        ('phone', DropdownFilter),
        # for choice fields
        # ('a_choicefield', ChoiceDropdownFilter),
        # for related fields
        ('customer', RelatedDropdownFilter),
    )


admin.site.register(CustomerPhone, CustomerPhoneAdmin)


class CustomerPhoneAdminInline(admin.TabularInline):
    model = CustomerPhone
    extra = 0
