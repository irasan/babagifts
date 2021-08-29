import uuid
from django.db import models
from django_countries.fields import CountryField

from datetime import datetime
from dateutil.relativedelta import relativedelta

from profiles.models import UserProfile


class Subscription(models.Model):
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    duration = models.IntegerField(default=1)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)

    def __str__(self):
        return self.name


class SubActive(models.Model):
    class Meta:
        ordering = ('-date',)
    
    description = models.CharField(max_length=80, null=False, blank=False, default='')
    sub_number = models.CharField(max_length=32, null=False, editable=False)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
                                     null=True, blank=True, related_name='subscriptions')
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    country = CountryField(blank_label='Country *', null=False, blank=False)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    county = models.CharField(max_length=80, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(default=datetime.now, null=False, blank=False)
    sub_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    stripe_pid = models.CharField(max_length=254, null=False, blank=False, default='')

    def _generate_sub_number(self):
        """
        Generate a random, unique subscription number using UUID
        """
        return uuid.uuid4().hex.upper()

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the subscription number
        if it hasn't been set already.
        """
        if not self.sub_number:
            self.sub_number = self._generate_sub_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.sub_number
