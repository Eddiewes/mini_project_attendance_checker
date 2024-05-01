from django.urls import path
from . import views

urlpatterns = [
    path('<add_event/', views.add_event, name='add_event'),
   


]


'''   path('event/<int:eventid>/', views.view_class, name='view_class'),'''