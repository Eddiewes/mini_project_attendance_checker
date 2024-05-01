
from django.contrib import admin
from django.urls import path,include
from core import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('<str:username>/', views.home, name='home'),
    path('<str:username>/', include('course.urls')),
    
    
]
