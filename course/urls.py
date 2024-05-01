from django.urls import path,include
from . import views
from classes import views as classes_views
urlpatterns = [
    path('addcourse/', views.add_course, name='add_course'),
    path('<str:coursename>/', views.view_course, name='view_course'),
   
    path('<str:coursename>/', include('classes.urls')),
]

''' path('<str:coursename>/addclass/', classes_views.add_class, name='add_class'),'''