from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from decimal import Decimal
from main_app.models import CreditCard
from account.models import Account

def card_detail(request, card_id):
    credit_card = CreditCard.objects.get(card_id=card_id, user=request.user)
    account = Account.objects.get(user=request.user)
    
    context = {
        "account":account,
        "credit_card":credit_card,
    }
    return render(request, "credit_card/card-detail.html", context)

def fund_card(request, card_id):
    credit_card = CreditCard.objects.get(card_id=card_id, user=request.user)
    account = Account.objects.get(user=request.user)
    
    if request.method == "POST":
        amount = request.POST.get("funding_amount")
        
        if Decimal(amount) <= account.account_balance:
            account.account_balance -= Decimal(amount)
            account.save()

            credit_card.amount += Decimal(amount)
            credit_card.save()
            
            messages.success(request, "Funding Successful")
            return redirect("main_app:card-detail", credit_card.card_id)
        else:
            messages.success(request, "Insufficient Funds")
            return redirect("main_app:card-detail", credit_card.card_id)
    
    context = {
        "account":account,
        "credit_card":credit_card,
    }
    return render(request, "credit_card/card-detail.html", context)
    

def withdraw_fund(request, card_id):
    credit_card = CreditCard.objects.get(card_id=card_id, user=request.user)
    account = Account.objects.get(user=request.user)
    
    if request.method == "POST":
        amount = request.POST.get("amount")

        if credit_card.amount >= Decimal(amount):
            account.account_balance += Decimal(amount)
            account.save()

            credit_card.amount -= Decimal(amount)
            credit_card.save()
            
            messages.success(request, "Withdrawal Successful")
            return redirect("main_app:card-detail", credit_card.card_id)
        else:
            messages.success(request, "Withdrawal Denied - Insufficient Funds")
            return redirect("main_app:card-detail", credit_card.card_id)


def delete_card(request, card_id):
    credit_card = CreditCard.objects.get(card_id=card_id, user=request.user)
    
    account = request.user.account
    
    if credit_card.amount > 0:
        account.account_balance += credit_card.amount
        account.save()
        
        credit_card.delete()
        messages.success(request, "Card Deleted Successfully")
        return redirect("account:dashboard")
    
    credit_card.delete()
    messages.success(request, "Card Deleted Successfully")
    return redirect("account:dashboard")