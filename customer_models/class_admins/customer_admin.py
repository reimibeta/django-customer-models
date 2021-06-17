from django.contrib import admin
from django_admin_listfilter_dropdown.filters import DropdownFilter, RelatedDropdownFilter
from django_html_render.html_render import HtmlRender

from customer_models.class_admins.customer_address_admin import CustomerAddressAdminInline
from customer_models.class_admins.customer_phone_admin import CustomerPhoneAdminInline
from customer_models.class_models.customer import Customer
from customer_models.class_models.customer_phone import CustomerPhone


class CustomerAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
        'priority',
        'customer_phone_numbers',
        'created_date',
        'customer_status',
        # 'customer_register_by'
    ]
    list_display_links = ['name', ]
    list_per_page = 25
    search_fields = [
        'name',
        'customer_phones__phone'
    ]

    def customer_status(self, obj):
        check = 'active' if obj.status else 'inactive'
        color = 'green' if obj.status else 'red'
        return HtmlRender.p(text=check, color=color)

    def customer_phone_numbers(self, obj):
        phones = []
        customer_phones = CustomerPhone.objects.filter(customer=obj.id)
        if customer_phones:
            for phone in customer_phones:
                phones.append(phone.phone)
        return ", ".join(phones)
        # separator = ', '
        # return separator.join(obj.customer_phones[0].phone)

    list_filter = (
        # for ordinary fields
        ('name', DropdownFilter),
        ('status', DropdownFilter),
        ('created_date', DropdownFilter),
        # ('customer_register_by__staff__user__name', DropdownFilter),
        # for choice fields
        # ('a_choicefield', ChoiceDropdownFilter),
        # for related fields
        ('customer_phones', RelatedDropdownFilter),
    )

    inlines = [
        CustomerAddressAdminInline,
        CustomerPhoneAdminInline,
        # CustomerRegisterByAdminInline
    ]


admin.site.register(Customer, CustomerAdmin)
