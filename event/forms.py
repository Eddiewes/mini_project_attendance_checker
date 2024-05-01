from django import forms
from .models import Event

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['event_name', 'start_time', 'end_time', 'location_address', 'geolocation', 'is_student_id_required', 'is_index_number_required', 'is_student_name_required']
        widgets = {
            'start_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'end_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

    event_name = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'placeholder': 'Event name (optional)',
        'class': 'form-control'
    }))

    location_address = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Event location',
        'class': 'form-control',
        'id': 'id_location_address'  # This ID is used by JavaScript for autocomplete
    }))