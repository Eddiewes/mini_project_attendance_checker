from django import forms
from .models import Course

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name']
        
    name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'The course name',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))    