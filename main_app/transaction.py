from django.shortcuts import render, redirect
from main_app.models import Transaction
from account.models import Account
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required
def transaction_list(request):
    sender_transaction = Transaction.objects.filter(sender=request.user, transaction_type="Transfer").order_by("-id")
    recipient_transaction = Transaction.objects.filter(recipient=request.user, transaction_type="Transfer").order_by("-id")
    
    request_sender_transaction = Transaction.objects.filter(sender=request.user, transaction_type="Request")
    request_recipient_transaction = Transaction.objects.filter(recipient=request.user, transaction_type="Request")
    
    deposit_transaction = Transaction.objects.filter(sender=request.user, transaction_type="Deposit")
    
    context = {
        "sender_transaction":sender_transaction,
        "recipient_transaction":recipient_transaction,
        
        "request_sender_transaction":request_sender_transaction,
        "request_recipient_transaction":request_recipient_transaction,
        
        "deposit_transaction": deposit_transaction,
    }
    
    return render(request, "transaction/transaction-list.html", context)

@login_required
def transaction_detail(request, transaction_id):
    transaction = Transaction.objects.get(transaction_id=transaction_id)
    
    context = {
        "transaction":transaction,
    }
    
    return render(request, "transaction/transaction-detail.html", context)