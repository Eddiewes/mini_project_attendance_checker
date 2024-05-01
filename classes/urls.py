from django.urls import path,include
from . import views


urlpatterns = [
    path('addclass/', views.add_class, name='add_class'),
    path('<str:classname>/', views.view_class, name='view_class'),
    path('<str:classname>/', include('event.urls')),
]