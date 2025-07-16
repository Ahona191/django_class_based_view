from django.shortcuts import render 
#from django.http import HttpResponse

# Create your views here. 
#def machine_learning(request): 
   #return render(request, 'machine_learning/machine_learning.html') 

def machine_learning(request):   
   course='machine learning' 
   Tclass=21 
   seat=20 
   cduration='2.5 months' 
   offering = {'c':course, 'tl':Tclass,'st':seat,'cd':cduration}
   offering = {'what' : 'lots of free and paid'}  

   teachers={'names': ['Shakil','Mejba','Sohan']} 
   return render(request, 'machine_learning/machine_learning.html', context=teachers) 

   #return render(request, 'machine_learning/machine_learning.html', context=offering)

def random(request): 
   return render(request, 'machine_learning/random_forest.html') 

def K_nearest(request): 
   return render(request, 'machine_learning/knn.html') 

def decision_tree(request): 
   return render(request, 'machine_learning/DT.html')



#def deep_learning(request): 
    #return HttpResponse('We have full deep learning course') 

#def about_us(request): 
    #return HttpResponse('I have experiencs')
    
