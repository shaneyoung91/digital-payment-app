from django.urls import path
from main_app import views, transfer

app_name = 'main_app'

urlpatterns = [
    path("", views.index, name='index'),
    
    # Transfers
    path("search-acct/", transfer.search_users_acct_number, name='search-acct'),
    path("amount-transfer/<account_number>/", transfer.amount_transfer, name='amount-transfer'),
    path("amount-transfer-process/<account_number>/", transfer.amount_transfer_process, name='amount-transfer-process'),
    path("transfer-confirmation/<account_number>/<transaction_id>/", transfer.transfer_confirmation, name='transfer-confirmation'),
    path("transfer-process/<account_number>/<transaction_id>/", transfer.transfer_process, name='transfer-process'),
    path("transfer-completed/<account_number>/<transaction_id>/", transfer.transfer_completed, name='transfer-completed'),
]
