from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='Home'),
    path('RegistrationView', views.RegistrationView.as_view()),
    path('LoginSerializerView', views.LoginSerializerView.as_view()),
    path('BasicInformationSerializerView', views.BasicInformationSerializerView.as_view()),
    path('NationalIdentificationNumberSerializerView', views.NationalIdentificationNumberSerializerView.as_view()),
    path('BankVerificationNumberSerializerView', views.BankVerificationNumberSerializerView.as_view()),
    path('NextOfKinSerializerView', views.NextOfKinSerializerView.as_view()),
]