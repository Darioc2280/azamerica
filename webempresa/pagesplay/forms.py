from django import forms
from .models import Page

class PageForm(forms.ModelForm):

    class Meta:
        model = Page
        fields = ['title', 'content', 'order', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'titulo'}),
            'content':forms.Textarea(attrs={'class':'form-control'}),
            'order': forms.NumberInput(attrs={'class':'form-control','placeholder':'orden'}),
            'image': forms.ClearableFileInput(attrs={'class':'form-control mt-3'}),
        }
        labels = {
            'title':'',
            'content': '',
            'order': '',
        }