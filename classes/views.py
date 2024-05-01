
from django.shortcuts import render, redirect, get_object_or_404
from .models import Class
from django.contrib.auth.decorators import login_required
from .forms import ClassForm
from course.models import Course
from event.models import Event
from django.contrib import messages
from core.models import Profile

def add_class(request, username, coursename):
    if request.method == 'POST':
        form = ClassForm(request.POST)
        if form.is_valid():
            course = get_object_or_404(Course, name=coursename)
            class_name = form.cleaned_data['class_name']
            if Class.objects.filter(course=course, class_name=class_name).exists():
                messages.error(request, 'A class with this name already exists for this course.')
            else:
                form.instance.course = course
                
                form.save()
                return redirect('view_course', username=username, coursename=coursename)
    else:
        form = ClassForm()
    return render(request, 'core/add_class.html', {'form': form})

def view_class(request, username, coursename, classname):
    # Get the class based on username, coursename, and classname
    profile = Profile.objects.get(user__username=username)
    class_obj = get_object_or_404(Class, course__name=coursename, class_name=classname)
    events = class_obj.event_set.all()  # Get all events related to this class
    return render(request, 'core/view_class.html', {'class': class_obj, 'events': events})