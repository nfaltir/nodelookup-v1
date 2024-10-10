from django import forms
from django.contrib.auth.models import User
from .models import Message

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['subject', 'content', 'status']  # Include status for admin only
        widgets = {
            'subject': forms.Select(attrs={'class': 'form-select block w-full p-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500'}),
            'content': forms.Textarea(attrs={'class': 'form-textarea block w-full p-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500', 'rows': 4}),
            'status': forms.Select(attrs={'class': 'form-select block w-full p-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500'}),
        }

    def __init__(self, *args, **kwargs):
        super(MessageForm, self).__init__(*args, **kwargs)
        if not kwargs.get('instance') or kwargs['instance'].sender != kwargs['instance'].recipient:
            self.fields['status'].disabled = True  # Disables status for normal users
