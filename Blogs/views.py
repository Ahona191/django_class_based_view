from django.shortcuts import render 
#from django.http import HttpResponse 
from . forms import TeachersRegistration

# Create your views here. 
def blog1(request): 
    return render(request,'blogs/blogs.html') 

def showformsdata(request):  
    if request.method =='POST': 
        fm=TeachersRegistration(request.POST) 
        #print(fm) 
        #print('This is POST statement')  
        if fm.is_valid():
         print(fm.cleaned_data['password'])   
         print(fm.cleaned_data['repassword']) 
         print('This is POST statement')
         

    else: 
     fm= TeachersRegistration()  
     print('This is GET statement') 
    return render(request, 'blogs/forms.html', {'form': fm})
