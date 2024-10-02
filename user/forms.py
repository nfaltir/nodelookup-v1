# forms.py
from django import forms


class RegistrationForm(forms.Form):
    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={
            'class': 'block w-full p-2 border border-gray-300 rounded-lg focus:outline-none focus:ring focus:ring-blue-500',
            'placeholder': 'Username'
        })
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'block w-full p-2 border border-gray-300 rounded-lg focus:outline-none focus:ring focus:ring-blue-500',
            'placeholder': 'Email'
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'block w-full p-2 border border-gray-300 rounded-lg focus:outline-none focus:ring focus:ring-blue-500',
            'placeholder': 'Password'
        })
    )
    password_confirm = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'block w-full p-2 border border-gray-300 rounded-lg focus:outline-none focus:ring focus:ring-blue-500',
            'placeholder': 'Confirm Password'
        })
    )
    
    # Custom validation to check if the passwords match
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")

        if password and password_confirm and password != password_confirm:
            self.add_error('password_confirm', "Passwords do not match.")
        return cleaned_data


#LOGIN FORM
class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={
            'class': 'block w-full p-2 border border-gray-300 rounded-lg mb-4 focus:outline-none focus:ring focus:ring-blue-500',
            'placeholder': 'Username'
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'block w-full p-2 border border-gray-300 rounded-lg focus:outline-none focus:ring focus:ring-blue-500',
            'placeholder': 'Password'
        })
    )