from django.http import HttpRequest
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import EventForm
from core.models import Profile
from classes.models import Class
from course.models import Course

def add_event(request: HttpRequest, username, coursename, classname):
    profile = Profile.objects.get(user__username=username)
    class_obj = Class.objects.get(course__name=coursename, class_name=classname)
    course = Course.objects.get(name=coursename, lecturer_profile=profile)

    if request.method == 'POST':
        form = EventForm(request.POST)
        # lng and lat
        lng = request.POST.get("lng")
        lat = request.POST.get("lat")
        if form.is_valid():
            
            event = form.save(commit=False)
            event.related_class = class_obj
            event.location_address = form.cleaned_data['location_address']
            event.geolocation = form.cleaned_data['geolocation']
            # Assign the class name and course name from the class object
           
            event.save()
            # Redirect to the 'view_class' URL with appropriate parameters
            return redirect('view_class', username=username, coursename=coursename, classname=classname)
        else:
            messages.error(request, 'Form validation failed. Please correct the errors.')
    else:
        form = EventForm()

    return render(request, 'core/add_event.html', {'form': form,'course': course} )
