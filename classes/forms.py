from django import forms
from .models import Class

class ClassForm(forms.ModelForm):
    
    class_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Class Name',
        'class': 'border w-full py-4 px-6 rounded-xl'
    }))
    description = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder': 'Class description (optional)',
        'class': 'border w-full py-4 px-6 rounded-xl',
        'rows': 1,  # Initial rows
    }), required=False)

    class Meta:
        model = Class
        fields = ['class_name','description']  
