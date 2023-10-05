from django.urls import path
from main_app import views, transfer, transaction, payment_request, credit_card, deposit

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
    path("delete-request/<account_number>/<transaction_id>/", payment_request.delete_payment_request, name="delete-request"),
    
    # Credit Card 
    path("card/<card_id>/", credit_card.card_detail, name="card-detail"),
    path("fund-card/<card_id>/", credit_card.fund_card, name="fund-card"),
    path("withdraw-fund/<card_id>/", credit_card.withdraw_fund, name="withdraw-fund"),
    path("delete-card/<card_id>/", credit_card.delete_card, name="delete-card"),
    
    # Deposit
    path('deposit-money/<account_number>/', deposit.deposit_money, name='deposit-money'),
    path("deposit-money-process/<account_number>/", deposit.deposit_money_process, name='deposit-money-process'),
    path('deposit-money-confirmation/<account_number>/<transaction_id>/', deposit.deposit_money_confirmation, name='deposit-money-confirmation'),
    path("deposit-process/<account_number>/<transaction_id>/", deposit.deposit_process, name='deposit-process'),
    path("deposit-completed/<account_number>/<transaction_id>/", deposit.deposit_completed, name='deposit-completed'),

]
