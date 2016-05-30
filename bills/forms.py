from django.utils import timezone
from django import forms
from .models import Bill, Item

class HostForm(forms.Form):
    bill_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'id': 'bill',
                'placeholder': 'Bill Name'
            }),
        required=True
    )

    item_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'id': 'name',
                'placeholder': 'Name'
            }),
        required=True
    )

    item_amount = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'id': 'amount',
                'placeholder': 'Amount'
            }),
        required=True
       )

    item_price = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'id': 'price',
                'placeholder': 'Price'
            }),
        required=True
    )

    def save(self):
        data = self.cleaned_data

        bill = Bill.objects.create(
            name=data['bill_name'],
            date=timezone.now()
        )

        item = Item.objects.create(
            bill=bill,
            name=data['item_name'],
            amount=data['item_amount'],
            price=data['item_price'],
        )
