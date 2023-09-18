from django.urls import path
from account import views

app_name = 'account'

urlpatterns = [
    path('kyc-reg/', views.kyc_registration, name='kyc-reg'),
]
