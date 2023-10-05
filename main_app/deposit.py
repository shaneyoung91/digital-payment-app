from django.shortcuts import render, redirect
from account.models import Account
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib import messages
from decimal import Decimal
from main_app.models import Transaction

@login_required
def deposit_money(request, account_number):
    account = Account.objects.get(account_number=account_number)
    
    context = {
        "account": account,
    }
    return render(request, "deposit/deposit-money.html", context)

def deposit_money_confirmation(request, account_number, transaction_id):
    try:
        account = Account.objects.get(account_number=account_number)
        transaction = Transaction.objects.get(transaction_id=transaction_id)
    except:
        messages.warning(request, "Transaction does not exist.")
        return redirect("account:dashboard")
    
    context = {
        "account": account,
        "transaction": transaction,
    }
    return render(request, "deposit/deposit-money-confirmation.html", context)

def deposit_money_process(request, account_number):
    account = Account.objects.get(account_number=account_number)
    
    if request.method == "POST":
        amount = request.POST.get("amount-deposit")
        
        new_transaction = Transaction.objects.create(
            user=request.user,
            sender=request.user,
            recipient=request.user,
            amount=amount,
            status="Processing",
            transaction_type="Deposit",            
        )
        new_transaction.save()
        
        transaction_id = new_transaction.transaction_id
        return redirect("main_app:deposit-money-confirmation", account.account_number, transaction_id)

    else:
        messages.warning(request, "An error occurred. Try again later.")
        return redirect("account:dashboard")


def deposit_process(request, account_number, transaction_id):
    account = Account.objects.get(account_number=account_number)
    transaction = Transaction.objects.get(transaction_id=transaction_id)

    if request.method == "POST":
        pin_number = request.POST.get("pin-number")
        
        if pin_number == account.pin_number:
            transaction.status = "Completed"
            transaction.save()
            
            account.account_balance += transaction.amount
            account.save()
        
            messages.success(request, "Deposit Successful!")
            return redirect("main_app:deposit-completed", account.account_number, transaction.transaction_id)
        
        else:
            messages.warning(request, "Incorrect Pin. Please try again.")
            return redirect("main_app:deposit-money-confirmation", account.account_number, transaction.transaction_id)
    else:
        messages.warning(request, "An error occurred. Try again later.")
        return redirect("account:dashboard")


def deposit_completed(request, account_number, transaction_id):
    try:
        account = Account.objects.get(account_number=account_number)
        transaction = Transaction.objects.get(transaction_id=transaction_id)
    except:
        messages.warning(request, "Transaction does not exist.")
        return redirect("account:dashboard")
    
    context = {
        "account": account,
        "transaction": transaction,
    }
    
    return render(request, "deposit/deposit-completed.html", context)