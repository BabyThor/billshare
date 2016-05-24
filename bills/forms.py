from django import forms

class HostForm(forms.Form):
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
