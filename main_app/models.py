from django.db import models
from userauths.models import User
from account.models import Account
from shortuuid.django_fields import ShortUUIDField
from django.core.validators import MinLengthValidator, MaxLengthValidator

# Create your models here.

TRANSACTION_TYPE = (
    ("Transfer", "Transfer"),
    ("Received", "Received"),
    ("Withdraw", "Withdraw"),
    ("Refund", "Refund"),
    ("Request", "Payment Request"),
    ("None", "None"),
)

TRANSACTION_STATUS = (
    ("Failed", "Failed"),
    ("Completed", "Completed"),
    ("Pending", "Pending"),
    ("Processing", "Processing"),
    ("Request Sent", "Request Sent"),
    ("Request Settled", "Request Settled"),
    ("Request Processing", "Request Processing"),
)

CARD_TYPE = (
    ("Mastercard", "Mastercard"),
    ("Visa", "Visa"),
    ("Discover", "Discover"),
    ("American Express", "American Express"),
)

class Transaction(models.Model):
    transaction_id = ShortUUIDField(unique=True, length=15, max_length=20, prefix="TRN")
    
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="user")
    amount = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    description = models.CharField(max_length=1000, null=True, blank=True)
    
    recipient = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="recipient")
    sender = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="sender")
    
    recipient_account = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True, related_name="recipient_account")
    sender_account = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True, related_name="sender_account")
    
    status = models.CharField(choices=TRANSACTION_STATUS, max_length=100, default="Pending")
    transaction_type = models.CharField(choices=TRANSACTION_TYPE, max_length=100, default="None")
    
    date = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    
    def __str__(self):
        try:
            return f"{self.user}"
        except:
            return f"Transaction"

class CreditCard(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    card_id = ShortUUIDField(unique=True, length=5, max_length=20, prefix="CARD", alphabet="1234567890")
    
    name = models.CharField(max_length=100)
    card_number = models.PositiveBigIntegerField()
    month = models.IntegerField()
    year = models.IntegerField()
    cvv = models.IntegerField()
    
    amount = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    
    card_type = models.CharField(choices=CARD_TYPE, max_length=50, default="Mastercard")
    card_status = models.BooleanField(default=True)
    
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user}"