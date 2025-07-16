from django.shortcuts import render 
from django.contrib.auth.forms import UserCreationForm
#from django.http import HttpResponse
# Create your views here.
def deep_learning(request):  
    return render(request,'deep_learning/deep_learning.html') 

#def registration(request): 
    #fm=UserCreationForm() 
    #return render (request, 'deep_learning/register.html', {'form': fm}) 

def registration(request):  
    if request.method =="POST": 
        fm=UserCreationForm(request.POST) 
        if fm.is_valid(): 
            fm.save() 
    else:  
        fm=UserCreationForm()

     
    return render (request, 'deep_learning/registration.html', {'form': fm})
    #return render(request, 'deep_learning/registration.html')  # or your correct template path
