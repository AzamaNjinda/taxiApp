from django.http import HttpResponse
from django.shortcuts import render
def homepage_taxi(request):
     return render(request,'taxi_homepage.html')