from django import forms

class PaymentForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    amount = forms.IntegerField(label="Amount (in ₹)")
