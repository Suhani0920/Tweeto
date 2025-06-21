from django import forms
from .models import Tweet

class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['text', 'photo']
        widgets = {
            'text': forms.Textarea(attrs={'rows': 3, 'placeholder': 'What\'s happening?'}),
            'photo': forms.ClearableFileInput(attrs={'multiple': True}),
        }
        labels = {
            'text': '',
            'photo': 'Add a photo (optional)',
        }
        help_texts = {
            'text': 'You can write up to 240 characters.',
        }