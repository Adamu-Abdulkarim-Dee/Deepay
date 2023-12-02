from django.urls import path
from . import views

urlpatterns = [
    path('create_withdraw', views.create_withdraw),
    path('get_debited_transaction', views.get_debited_transaction),
    path('get_credited_transaction', views.get_credited_transaction),
    path('account', views.account),
]