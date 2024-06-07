from django import forms
from .models import Quote, AuthUser
from django.core.validators import RegexValidator
from django.contrib.auth.hashers import make_password



class QuoteForm(forms.ModelForm):
    class Meta:
        model = Quote
        fields = ['departure', 'delivery', 'weight', 'dimensions', 'name', 'email', 'phone', 'message']



class AuthUserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(), validators=[
        RegexValidator(
            r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[!@#$%^&*(),.?":{}|<>])[A-Za-z\d!@#$%^&*(),.?":{}|<>]{8,}$',
            message='Password must contain at least one uppercase letter, one lowercase letter, one digit, one special character, and be at least 8 characters long.'
        )
    ])
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = AuthUser
        fields = ['username', 'first_name', 'last_name', 'email', 'phone_number', 'password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and password != confirm_password:
            self.add_error('confirm_password', "Passwords do not match.")
        
        cleaned_data['password'] = make_password(password)
        return cleaned_data