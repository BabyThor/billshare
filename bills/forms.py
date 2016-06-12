from django.utils import timezone
from django import forms
from .models import Bill, Item

class HostForm(forms.Form):
    bill_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'id': 'bill',
                'placeholder': 'Bill Name',
                'required': True,
            }),
        required=True
    )

    item_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'name',
                'placeholder': 'Name',
                'required': True,
            }),
        required=True
    )

    item_amount = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'amount',
                'placeholder': 'Amount',
                'required': True,
            }),
        initial=1,
        required=True
       )

    item_price = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'price',
                'placeholder': 'Price',
                'required': True,
            }),
        required=True
    )
