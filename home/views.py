from django.shortcuts import render, redirect, reverse
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings


# Create your views here.
def index(request):
    """ A view to return the index page """
    if request.method == 'POST':
        user_email = request.POST.get('email')
        subject = "New newsletter Subscriber"
        message = "Please add this email address to your newsletter"

        if user_email.is_valid():
            send_mail(
                subject,
                message,
                user_email,
                [settings.DEFAULT_FROM_EMAIL],
                )

            messages.success(request, 'Your message has been sent!')
            return redirect(reverse('contact'))
        else:
            messages.error(request, 'Message was not sent. Try again.')

    return render(request, 'home/index.html')
