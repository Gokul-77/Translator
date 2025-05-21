from django import forms
from googletrans import LANGUAGES

LANG_CHOICES = [(k, v.title()) for k, v in LANGUAGES.items()]

class TranslateForm(forms.Form):
    text = forms.CharField(label='Enter Your Text', widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'Type text here...',
        'rows': 3
    }))
    dest_lang = forms.ChoiceField(label='To Which Language', choices=LANG_CHOICES, widget=forms.Select(attrs={
        'class': 'form-select'
    }))
