from django.shortcuts import render
from django.http import HttpResponse
from . models import Place
from . models import Meet
# Create your views here.





def index(request):
    obj=Meet.objects.all()
    obj1=Place.objects.all()
    return render(request,"index.html",{'result':obj,'result1': obj1})