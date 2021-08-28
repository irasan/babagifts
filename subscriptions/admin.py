from django.contrib import admin
from .models import SubActive, Subscription


class SubActiveAdmin(admin.ModelAdmin):

    readonly_fields = ('sub_number', 'date',
                       'sub_total', 'stripe_pid')

    fields = ('sub_number', 'user_profile', 'date', 'full_name',
              'email', 'phone_number', 'country',
              'postcode', 'town_or_city', 'street_address1',
              'street_address2', 'county', 'sub_total', 'stripe_pid')

    list_display = ('sub_number', 'date', 'full_name',
                    'sub_total',)

    ordering = ('-date',)


admin.site.register(SubActive, SubActiveAdmin)
admin.site.register(Subscription)
