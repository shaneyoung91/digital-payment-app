from django.urls import path
from main_app import views, transfer

app_name = 'main_app'

urlpatterns = [
    path("", views.index, name='index'),
    
    # Transfers
    path("search-acct/", transfer.search_users_acct_number, name='search-acct'),
    path("amount-transfer/<account_number>/", transfer.amount_transfer, name='amount-transfer'),
]
