from django.shortcuts import render  
from django.views import View
#from django.http import HttpResponse
def data_analysis(request):  
    return render(request,'data_analysis/analysis.html') 
# Create your views here. 

class DataAnalysis(View): 
    def get(self, request): 
        return render(request,'data_analysis/class.html')
