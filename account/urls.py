from django.urls import path
from account import views

app_name = 'account'

urlpatterns = [
    path('', views.account, name='account'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('kyc-reg/', views.kyc_registration, name='kyc-reg'),
]
