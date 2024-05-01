from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth import login as auth_login
from .forms import SignUpForm,LoginForm
from django.contrib.auth import authenticate
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from course.models import Course
from . models import Profile




def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        
        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect('signup')
            else:
                # Create the user
                user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email, password=password)
                
                # Create the profile for the user
                Profile.objects.create(user=user)
                
                messages.success(request, 'Account created successfully. Please log in.')
                return redirect('login')
        else:
            messages.error(request, 'Passwords do not match')
            return redirect('signup')
    else:
        return render(request, 'core/signup.html')


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                # Retrieve the Profile instance for the authenticated user
                try:
                    profile = Profile.objects.get(user=user)
                except Profile.DoesNotExist:
                    # Handle the case where profile does not exist (create if necessary)
                    profile = Profile.objects.create(user=user)
                # Redirect to 'home' passing the username as an argument
                return redirect('home', username=profile.user.username)
            else:
                form.add_error(None, 'Invalid username or password')
    else:
        form = LoginForm()
    return render(request, 'core/login.html', {'form': form})

@login_required
def home(request, username):
    profile = Profile.objects.get(user__username=username)
    courses = Course.objects.filter(lecturer_profile=profile)
    return render(request, 'core/home.html', {'profile': profile, 'courses': courses})