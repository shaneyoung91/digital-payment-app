from django.urls import path
from main_app import views, transfer, transaction, payment_request

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
    
    # Transactions
    path("transactions/", transaction.transaction_list, name="transactions"),
    path("transaction-detail/<transaction_id>/", transaction.transaction_detail, name="transaction-detail"),
    
    # Payment Request
    path("request-search-acct/", payment_request.search_users_request, name="request-search-acct"),
    path("amount-request/<account_number>/", payment_request.amount_request, name="amount-request"),
    path("amount-request-process/<account_number>/", payment_request.amount_request_process, name="amount-request-process"),
    path("amount-request-confirmation/<account_number>/<transaction_id>/", payment_request.amount_request_confirmation, name="amount-request-confirmation"),
    path("amount-request-final-process/<account_number>/<transaction_id>/", payment_request.amount_request_final_process, name="amount-request-final-process"),
    path("amount-request-completed/<account_number>/<transaction_id>/", payment_request.amount_request_completed, name="amount-request-completed"),
    
    # Request Settlement
    path("settlement-confirmation/<account_number>/<transaction_id>/", payment_request.settlement_confirmation, name="settlement-confirmation"),
    path("settlement-processing/<account_number>/<transaction_id>/", payment_request.settlement_processing, name="settlement-processing"),
    path("settlement-completed/<account_number>/<transaction_id>/", payment_request.settlement_completed, name="settlement-completed"),
]
