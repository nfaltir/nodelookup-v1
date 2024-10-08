from django import forms
from .models import UserRequest

class UserRequestForm(forms.ModelForm):
    class Meta:
        model = UserRequest
        fields = ['channel_name', 'channel_link', 'channel_id', 'channel_industry', 'specific_questions']
        widgets = {
            'channel_name': forms.TextInput(attrs={
                'class': 'block w-full p-2 border border-gray-300 rounded-lg',
                'placeholder': 'Channel Name'
            }),
            'channel_link': forms.URLInput(attrs={
                'class': 'block w-full p-2 border border-gray-300 rounded-lg',
                'placeholder': 'Channel Link'
            }),
            'channel_id': forms.TextInput(attrs={
                'class': 'block w-full p-2 border border-gray-300 rounded-lg',
                'placeholder': 'Channel ID'
            }),
            'channel_industry': forms.Select(attrs={
                'class': 'block w-full p-2 border border-gray-300 rounded-lg',
            }),
            'specific_questions': forms.Textarea(attrs={
                'class': 'block w-full p-2 border border-gray-300 rounded-lg',
                'placeholder': 'Any specific insights you want the research to find?'
            }),
        }
