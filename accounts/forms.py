from django import forms
from .models import User


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['display_name', 'bio']

        widgets = {
            'display_name': forms.TextInput(attrs={
                'placeholder': 'How should we display your name?',
            }),
            'bio': forms.Textarea(attrs={
                'placeholder': 'Tell people a little about yourself...',
                'rows': 4,
            }),
        }