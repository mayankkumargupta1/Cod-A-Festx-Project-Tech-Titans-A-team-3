from django import forms
from . models import *

class TextGenerationForm(forms.Form):
    prompt = forms.CharField(label='Tell me your problem:', max_length=255, widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': 'Type something...'
    }))

class AskDoctorForm(forms.ModelForm):
    class Meta:
        model = ask_doctor
        fields = ['question']
        widgets = {
            'question': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Ask your question...'}),
        }