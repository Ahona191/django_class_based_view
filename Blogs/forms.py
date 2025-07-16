from django import forms  
from django.core import validators

class TeachersRegistration(forms.Form): 
    first_name= forms.CharField(label='Enter Your First Name', label_suffix=' ') 
    last_name= forms.CharField(initial='Study Mart') 
    email= forms.EmailField(initial='ahona9168@gmail.com', disabled=True) 
    password=forms.CharField(widget=forms.PasswordInput)  
    repassword=forms.CharField(widget=forms.PasswordInput) 
    textarea=forms.CharField(widget=forms.Textarea) 
    file=forms.CharField(widget=forms.FileInput) 
    checkbox=forms.CharField(widget=forms.CheckboxInput) 

    def clean(self):
        cleaned_data = super().clean() 
        rightpass= self.cleaned_data['password'] 
        wrongpass= self.cleaned_data['repassword'] 
        if rightpass != wrongpass :
           raise forms.ValidationError('Password does not match')