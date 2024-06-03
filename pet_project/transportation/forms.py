from django import forms
from .models import Quote, Users

class QuoteForm(forms.ModelForm):
    class Meta:
        model = Quote
        fields = ['departure', 'delivery', 'weight', 'dimensions', 'name', 'email', 'phone', 'message']



class UserRegistrationForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = Users
        fields = ['username', 'email', 'password_hash', 'first_name', 'last_name', 'address', 'phone_number']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password_hash")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")

        return cleaned_data