from django.contrib import admin
from .models import SubActive, Subscription


class SubActiveAdmin(admin.ModelAdmin):

    readonly_fields = ('sub_number', 'date',
                       'sub_total', 'stripe_pid')

    fields = ('sub_number', 'user_profile', 'date', 'description', 
              'full_name', 'email', 'phone_number', 'country',
              'postcode', 'town_or_city', 'street_address1',
              'street_address2', 'county', 'sub_total', 'stripe_pid')

    list_display = ('sub_number', 'date', 'description', 'full_name',
                    'sub_total',)

    ordering = ('-date',)


class SubscriptionAdmin(admin.ModelAdmin):

    list_display = ('sku', 'name', 'price', 'duration')

    ordering = ('sku',)


admin.site.register(SubActive, SubActiveAdmin)
admin.site.register(Subscription, SubscriptionAdmin)
