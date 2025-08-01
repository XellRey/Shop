from django import forms
from .models import Order
from accounts.models import Addresses
class OrderCreateForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = ["address"]

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user is not None:
            self.fields['address'].queryset = Addresses.objects.filter(user=user)
