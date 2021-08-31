from django.urls import path
from . import views
from .webhooks import webhook


urlpatterns = [
    path('', views.all_subscriptions, name='all_subscriptions'),
    path('<int:subscription_id>/', views.subscribe, name='subscribe'),
    path('confirm_sub/<sub_number>', views.confirm_sub, name='confirm_sub'),
    path('cache_subscribe_data/', views.cache_subscribe_data, name='cache_subscribe_data'),
    path('wh/', webhook, name='webhook'),
]
