

from django import forms
from .models import UploadedContent

class UploadContentForm(forms.ModelForm):
    class Meta:
        model = UploadedContent
        fields = ['photo', 'file']
        labels = {
            'photo': 'Upload Photo',
            'file': 'Upload File',
        }



