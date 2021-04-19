from django import forms
from django.forms import ModelForm

from .models import Transactions

class MoneyTransferForm(ModelForm):
    class Meta:
        model = Transactions
        fields = ['sender', 'receiver', 'amount']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["sender"].widget.attrs.update({"class": "w3-select"})
        self.fields["receiver"].widget.attrs.update({"class": "w3-select"})
