from django.db import models
from classes.models import Class
from django_google_maps.fields import AddressField, GeoLocationField  
from django.utils.translation import gettext_lazy as _

class Event(models.Model):
    event_id = models.AutoField(primary_key=True)
    related_class = models.ForeignKey(Class, on_delete=models.CASCADE)
    event_name = models.CharField(max_length=100, blank=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    location_address = AddressField(max_length=200,null=True)
    geolocation = GeoLocationField(max_length=100,null=True)
    radius = models.DecimalField(_("Radius"), max_digits=5, decimal_places=2)
    is_student_id_required = models.BooleanField(default=False)
    is_index_number_required = models.BooleanField(default=False)
    is_student_name_required = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if self.event_name:
            return self.event_name
        else:
            return f"Event ID: {self.event_id}" 
    
    class Meta:
        ordering = ['-created_at']
