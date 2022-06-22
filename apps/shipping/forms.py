""" apps.shipping/forms.py """
from django import forms
from apps.shipping.models import Shipping


class ShippingForm(forms.ModelForm):

	class Meta:
		model = Shipping
		fields = ['type', 'charge']
		widgets = {
			'type' : forms.TextInput(attrs = {'class': 'form-control'}),
			'charge': forms.NumberInput(attrs = {'class': 'form-control'})
		}
