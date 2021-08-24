from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_subscriptions, name='subscriptions'),
    path("confirm-sub/", views.confirm_sub, name="confirm_sub"),
]
