from django.http import HttpResponse
from django.shortcuts import render
from . models import place
from . models import details
# Create your views here.

def fun(request):
    obj=place.objects.all()
    obj1=details.objects.all()

    return render(request,"index.html",{'results':obj,'results1':obj1})



