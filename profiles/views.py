from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import UserProfileForm
from wishlists.contexts import wishlist_count

from .models import UserProfile
from checkout.models import Order
from subscriptions.models import SubActive


@login_required
def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)
    count = wishlist_count(request)['items_count']

    # Update user's info
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, 'Update failed. Please ensure the \
                form is valid.')
    else:
        form = UserProfileForm(instance=profile)
    orders = profile.orders.all()
    orders.order_by('-date')
    subscriptions = profile.subscriptions.all()

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'subscriptions': subscriptions,
        'wishlist_count': count,
    }

    return render(request, template, context)


@login_required
def order_history(request, order_number):
    """ A view to display user's previous orders """

    order = get_object_or_404(Order, order_number=order_number)
    profile = get_object_or_404(UserProfile, user=request.user)

    if profile:
        if order.user_profile == profile:
            messages.info(request, (f'This is a past confirmation \
                for order number {order_number}. A confirmation \
                email was sent on the order date.'))

            template = 'checkout/checkout_success.html'
            context = {
                'order': order,
                'from_profile': True,
            }

            return render(request, template, context)

        else:
            return(redirect('profile'))
    else:
        return(redirect('home'))


def sub_history(request, sub_number):
    """ A view to display user's subscriptions """

    sub_active = get_object_or_404(SubActive, sub_number=sub_number)
    messages.info(request, (
        f'This is a past confirmation for subscription number {sub_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'subscriptions/confirm_sub.html'
    context = {
        'sub_active': sub_active,
        'from_profile': True,
    }

    return render(request, template, context)


# Back up function for logging out
def auth_logout(request):
    logout(request)
    return redirect('home')
