from django.db import models
from profiles.models import UserProfile
from products.models import Product


class Wishlist(models.Model):
    """
    Model to create a wishlist and wishlist item
    """
    user = models.ForeignKey(UserProfile, null=False, blank=False,
                             on_delete=models.CASCADE, related_name='wishlist')

    def __str__(self):
        return self.user


class WishlistItem(models.Model):

    wishlist = models.ForeignKey(Wishlist, null=False, blank=False,
                                 on_delete=models.CASCADE,
                                 related_name='wishlist_item')

    product = models.ForeignKey(Product, null=False, blank=False,
                                on_delete=models.CASCADE,
                                related_name='product')

    def __str__(self):
        return self.product
