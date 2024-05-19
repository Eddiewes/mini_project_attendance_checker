from django import forms
from django.contrib.admin.options import widgets
from .models import Event

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['event_name', 'start_time', 'end_time', 'location_address', 'geolocation', 'radius' ,'is_student_id_required', 'is_index_number_required', 'is_student_name_required']
        widgets = {
            'start_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'end_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            # "radius": forms.CharField()
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

    radius = forms.DecimalField(required=True, widget=forms.TextInput(attrs={
        'id':'radius',
        'type':'number'
        }))
