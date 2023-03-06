from django import forms
from .models import TextModel, Attachment


class PostForm(forms.ModelForm):
    class Meta:
        model = TextModel
        fields = ['text', 'attachments']
        widgets = {
            'text': forms.Textarea(attrs={'class': 'form-control'}),
            'attachments': forms.ClearableFileInput(attrs={'multiple': True}),
        }
