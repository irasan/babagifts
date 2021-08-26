from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings

from .forms import SubscriptionForm
from .models import Subscription, SubActive

from profiles.models import UserProfile

import stripe
import json



# Create your views here.
def all_subscriptions(request):
    """ A view to return the subscriptions page """

    subscriptions = Subscription.objects.all()
    context = {
        'subscriptions': subscriptions,
    }

    return render(request, 'subscriptions/all_subscriptions.html', context)


@require_POST
def cache_subscribe_data(request):
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Sorry, your payment cannot be \
            processed right now. Please try again later.')
        return HttpResponse(content=e, status=400)


def subscribe(request, subscription_id):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    subscription = get_object_or_404(Subscription, pk=subscription_id)

    if request.method == 'POST':
        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'duration': request.POST['duration'],
            'phone_number': request.POST['phone_number'],
            'country': request.POST['country'],
            'postcode': request.POST['postcode'],
            'town_or_city': request.POST['town_or_city'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'county': request.POST['county'],
        }

        subscription_form = SubscriptionForm(form_data)
        if subscription_form.is_valid():
            sub_active = subscription_form.save()
            pid = request.POST.get('client_secret').split('_secret')[0]
            sub_active.stripe_pid = pid
            sub_active.save()
            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('confirm_sub', args=[sub_active.sub_number]))

        else:
            messages.error(request, 'There was an error with your form. \
                Please double check your information.')

    else:
        fee = round(subscription.price * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=fee,
            currency=settings.STRIPE_CURRENCY,
        )
        """ A view that renders the subscribe page """
        subscription_form = SubscriptionForm()

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. \
            Did you forget to set it in your environment?')

    template = 'subscriptions/subscribe.html'
    context = {
        'subscription_form': subscription_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
        'subscription': subscription,
    }

    return render(request, template, context)


def confirm_sub(request, sub_number):
    """
    Handle successful subscribes
    """

    template = 'subscriptions/confirm_sub.html'

    return render(request, template)
