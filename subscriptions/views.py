from django.shortcuts import render
from .models import Subscription


# Create your views here.
def all_subscriptions(request):
    """ A view to return the subscriptions page """

    subscriptions = Subscription.objects.all()
    context = {
        'subscriptions': subscriptions,
    }

    return render(request, 'subscriptions/subscriptions.html', context)


def confirm_sub(request):

    return render(request, 'subscriptions/confirm_sub.html')
