from django.shortcuts import render
from django.http import HttpResponse
from .models import *




def Home(request):
  return render(request,'index.html')


def Search(request):
    if request.method == 'POST': 
        category = request.POST.get('category')
        category = category.capitalize()
        print('22222222222222',category)
        mydata = companies.objects.filter(category = category).values()
        print("5555555",mydata)
      #   data = companies.objects.all().values()
        output = []
        for x in mydata:
           output.append(x) 
    return render(request,'page.html',{'output': output})
        
   
   


