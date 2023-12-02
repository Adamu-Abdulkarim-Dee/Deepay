from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='Home'),
    path('get_all', views.get_all),
    path('RegistrationView', views.RegistrationView.as_view()),
    path('LoginSerializerView', views.LoginSerializerView.as_view()),
    path('create_basic_information', views.create_basic_information),
    path('validate_nin_number', views.validate_nin_number),
    path('validate_bvn_number', views.validate_bvn_number),
    path('create_next_of_king', views.create_next_of_king),
]