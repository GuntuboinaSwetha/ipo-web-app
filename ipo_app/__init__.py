from django import forms
from .models import IPO

class IPOForm(forms.ModelForm):
    class Meta:
        model = IPO
        fields = '__all__'
        widgets = {
            'open_date': forms.TextInput(attrs={'readonly': 'readonly'}),
            'close_date': forms.TextInput(attrs={'readonly': 'readonly'}),
            'price_band': forms.TextInput(attrs={'readonly': 'readonly'}),
            'listing_date': forms.TextInput(attrs={'readonly': 'readonly'}),
        }
