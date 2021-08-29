from django.shortcuts import render, redirect, get_object_or_404, reverse, HttpResponseRedirect
from django.contrib import messages
from .models import UserProfile, Product, Wishlist, WishlistItem
from django.contrib.auth.decorators import login_required


@login_required
def view_wishlist(request):
    """
    View to display wishlist on a separate page
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


@login_required
def add_to_wishlist(request, product_id):
    """
    View to add products to wishlist
    """
    user = get_object_or_404(UserProfile, user=request.user)
    product = get_object_or_404(Product, pk=product_id)
    try:
        wishlist = Wishlist.objects.get(user=user)
    except:
        wishlist = None

    if wishlist:
        if WishlistItem.objects.filter(product=product).exists():
            messages.add_message(request, messages.ERROR, "You already have it in your wishlist.")
            return HttpResponseRedirect(reverse('view_wishlist'))
    
        wishlist_item = WishlistItem.objects.create(wishlist=wishlist, product=product)
        wishlist_item.save()
        messages.success(
            request, f'Added {product.name} to your wishlist')
    else:
        wishlist = Wishlist.objects.create(user=user)
        if WishlistItem.objects.filter(product=product).exists():
            messages.error(request, f'You already have {product.name} in your wishlist.')
            
            return HttpResponse(status=500)
    
        wishlist_item = WishlistItem.objects.create(wishlist=wishlist, product=product)
        wishlist_item.save()
        messages.success(
            request, f'Added {product.name} to your wishlist')
    return redirect(reverse('view_wishlist'))


@login_required
def remove_from_wishlist(request, product_id):
    """
    View to add products to wishlist
    """
    product = get_object_or_404(Product, pk=product_id)
    user = get_object_or_404(UserProfile, user=request.user)
    wishlist = wishlist = user.wishlist.all()
    wishlist_item = WishlistItem.objects.filter(product=product,
                                                wishlist__in=wishlist).delete()
    messages.success(request, f'Product {product.name} removed form wishlist!')

    return redirect(reverse('view_wishlist'))
