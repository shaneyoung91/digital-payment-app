from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
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