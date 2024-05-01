from django.shortcuts import render, redirect
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .models import Course
from classes.models import Class
from core.models import Profile
from django.contrib.auth.decorators import login_required
from .forms import CourseForm

@login_required
def add_course(request, username):
    profile = Profile.objects.get(user__username=username)
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            course_name = form.cleaned_data['name']
            if Course.objects.filter(name=course_name, lecturer_profile=profile).exists():
                messages.error(request, f'A course with the name "{course_name}" already exists for your profile.')
            else:
                course = form.save(commit=False)
                course.lecturer_profile = profile
                course.save()
                messages.success(request, f'Course "{course_name}" created successfully.')
                return redirect('home', username=username)
    else:
        form = CourseForm()
    return render(request, 'core/add_course.html', {'form': form})

@login_required
def view_course(request, username, coursename):
    profile = Profile.objects.get(user__username=username)
    course = get_object_or_404(Course, name=coursename, lecturer_profile=profile)
    classes = Class.objects.filter(course=course)
    return render(request, 'core/view_course.html', {'course': course, 'classes': classes})