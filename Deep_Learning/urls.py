from django.contrib import admin 

from django.urls import path 
from . import views

urlpatterns = [
     
    path('DL/', views.deep_learning, name='deep'),  
    path('register/', views.registration)
    
    
    
]