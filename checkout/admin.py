from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = ('order_number', 'start_date', 'end_date',
                       'total', 'stripe_pid')

    fields = ('order_number', 'user_profile', 'full_name',
              'email', 'phone_number', 'country',
              'post_code', 'town_or_city', 'street_address1',
              'street_address2', 'county', 'start_date',
              'end_date', 'plan_active', 'total',
              'stripe_pid', 'original_cart')

    ordering = ('-start_date',)


admin.site.register(Order, OrderAdmin)
