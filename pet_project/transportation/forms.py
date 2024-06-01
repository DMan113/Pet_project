from django import forms
from .models import Quote

class QuoteForm(forms.ModelForm):
    class Meta:
        model = Quote
        fields = ['departure', 'delivery', 'weight', 'dimensions', 'name', 'email', 'phone', 'message']