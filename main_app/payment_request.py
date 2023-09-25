from django.shortcuts import render, redirect
from account.models import Account
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib import messages
from decimal import Decimal
from main_app.models import Transaction

@login_required
def search_users_request(request):
    account = Account.objects.all()
    query = request.POST.get("account_number") ## <input name="account_number">
    
    if query:
        account = account.filter(
            Q(account_number=query)|
            Q(account_id=query)
        ).distinct()
    
    context = {
        "account": account,
        "query": query,
    }
    
    return render(request, "payment_request/search-users.html", context)

def amount_request(request, account_number):
    account = Account.objects.get(account_number=account_number)
    context = {
        "account": account,
    }
    return render(request, "payment_request/amount-request.html", context)

def amount_request_process(request, account_number):
    account = Account.objects.get(account_number=account_number)
    
    sender = request.user
    recipient = account.user
    
    sender_account = request.user.account
    recipient_account = account
    
    if request.method == "POST":
        amount = request.POST.get("amount-request") # input name
        description = request.POST.get("description")  # input name
        
        new_request = Transaction.objects.create(
            user = request.user,
            amount = amount,
            description = description,
            
            sender = sender,
            recipient = recipient,
            
            sender_account=sender_account,
            recipient_account=recipient_account,
            
            status="Request Processing",
            transaction_type="Request",
        )
        new_request.save()
        transaction_id = new_request.transaction_id
        return redirect("main_app:amount-request-confirmation", account.account_number, transaction_id)
    else:
        messages.warning(request, "An error occurred. Try again later!")
        return redirect("account:dashboard")

def amount_request_confirmation(request, account_number, transaction_id):
    account = Account.objects.get(account_number=account_number)
    transaction = Transaction.objects.get(transaction_id=transaction_id)
    context = {
        "account": account,
        "transaction": transaction,
    }
    return render(request, "payment_request/amount-request-confirmation.html", context)

def amount_request_final_process(request, account_number, transaction_id):
    account = Account.objects.get(account_number=account_number)
    transaction = Transaction.objects.get(transaction_id=transaction_id)
    
    if request.method == "POST":
        pin_number = request.POST.get("pin-number")
        if pin_number == request.user.account.pin_number:
            transaction.status = "Request Sent"
            transaction.save()
            
            messages.success(request, "Your payment request has been sent successfully.")
            return redirect("main_app:amount-request-completed", account.account_number, transaction.transaction_id)
    else:
        messages.warning(request, "An error occurred. Try again later!")
        return redirect("account:dashboard")

def amount_request_completed(request, account_number, transaction_id):
    account = Account.objects.get(account_number=account_number)
    transaction = Transaction.objects.get(transaction_id=transaction_id)
    
    context = {
        "account": account,
        "transaction": transaction,
    }
    return render(request, "payment_request/amount-request-completed.html", context)


## Settlement Functions
def settlement_confirmation(request, account_number, transaction_id):
    account = Account.objects.get(account_number=account_number)
    transaction = Transaction.objects.get(transaction_id=transaction_id)
    
    context = {
        "account": account,
        "transaction": transaction,
    }
    return render(request, "payment_request/settlement-confirmation.html", context)

def settlement_processing(request, account_number, transaction_id):
    account = Account.objects.get(account_number=account_number)
    transaction = Transaction.objects.get(transaction_id=transaction_id)
    
    sender = request.user
    sender_account = request.user.account
    
    if request.method == "POST":
        pin_number = request.POST.get("pin-number")
        if pin_number == request.user.account.pin_number:
            if sender_account.account_balance <= 0 or sender_account.account_balance < transaction.amount:
                messages.warning(request, "Insufficient Funds")
            else:
                sender_account.account_balance -= transaction.amount
                sender_account.save()
                
                account.account_balance += transaction.amount
                account.save()
                
                transaction.status = "Request Settled"
                transaction.save()
                
                messages.success(request, f"Request to {account.user.kyc.full_name} was successful.")
                return redirect("main_app:settlement-completed", account.account_number, transaction.transaction_id)
        else:
            messages.warning(request, "Incorrect Pin. Please try again.")
            return redirect("main_app:settlement-confirmation", account.account_number, transaction.transaction_id)
    else:
        messages.warning(request, "An error occurred. Try again later.")
        return redirect("account:dashboard")


def settlement_completed(request, account_number, transaction_id):
    account = Account.objects.get(account_number=account_number)
    transaction = Transaction.objects.get(transaction_id=transaction_id)
    
    context = {
        "account": account,
        "transaction": transaction,
    }
    return render(request, "payment_request/settlement-completed.html", context)