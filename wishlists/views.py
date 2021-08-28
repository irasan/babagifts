from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib import messages
from .models import UserProfile, Product, Wishlist, WishlistItem
from django.contrib.auth.decorators import login_required


@login_required
def view_wishlist(request):
    """
    View to display wishlist
    """
    user = get_object_or_404(UserProfile, user=request.user)
    wishlist = user.wishlist.all()

    if wishlist:
        wishlist_items = WishlistItem.objects.filter(wishlist__in=wishlist)

    else:
        wishlist_items = []

    template = 'wishlists/wishlist.html'
    context = {
        'wishlist_items': wishlist_items,
    }
    return render(request, template, context)

