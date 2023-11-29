from django.urls import path
from . import views

urlpatterns = [
    path('transfer', views.transfer),
    path('TransactionalView', views.TransactionalView.as_view()),
    path('AccountView', views.AccountView.as_view()),
]