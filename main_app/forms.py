from django import forms
from main_app.models import CreditCard

class CreditCardForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Card Holder Name"}))
    card_number = forms.IntegerField(widget=forms.NumberInput(attrs={"placeholder":"Card Number"}))
    month = forms.IntegerField(widget=forms.NumberInput(attrs={"placeholder":"MM"}))
    year = forms.IntegerField(widget=forms.NumberInput(attrs={"placeholder":"YY"}))
    cvv = forms.IntegerField(widget=forms.NumberInput(attrs={"placeholder":"****"}))
    
    class Meta:
        model = CreditCard
        fields = ['name', 'card_number', 'month', 'year', 'cvv', 'card_type']