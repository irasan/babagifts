from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_subscriptions, name='all_subscriptions'),
    path('<int:subscription_id>/', views.subscribe, name='subscribe'),
    path('confirm_sub/<sub_number>', views.confirm_sub, name='confirm_sub'),
    path('cache_checkout_data/', views.cache_subscribe_data, name='cache_subscribe_data'),
]
