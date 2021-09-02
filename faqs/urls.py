from django.urls import path
from . import views

urlpatterns = [
    path('', views.frequent_questions, name='frequent_questions')
]
