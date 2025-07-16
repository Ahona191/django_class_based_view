from django.contrib import admin 

from django.urls import path 
from . import views

urlpatterns = [
     
    path('ML/', views.machine_learning, name='ml_home'),  
    path('rn/', views.random, name='rf'), 
    path('knn/', views.K_nearest, name='knn'), 
    path('dt/', views.decision_tree, name='dt'),
   # path('dl/', views.deep_learning),  
   # path('about/', views.about_us),
    
    
]
