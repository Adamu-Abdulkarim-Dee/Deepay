from django.urls import path
from . import views

urlpatterns = [
    path('create_withdraw', views.create_withdraw),
    path('get_receiver_transaction', views.get_receiver_transaction),
    path('get_sender_transaction', views.get_sender_transaction),
    path('account', views.account),
]