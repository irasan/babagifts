from django.shortcuts import get_object_or_404
from .models import UserProfile, WishlistItem


def wishlist_count(request):

    count = 0
    user = get_object_or_404(UserProfile, user=request.user)
    wishlist = user.wishlist.all()

    if wishlist:
        count = WishlistItem.objects.filter(wishlist__in=wishlist).count()

    context = {
        'items_count': count,
    }

    return context
