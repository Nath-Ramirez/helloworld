from django.shortcuts import render
from django.http import HttpResponse #new

# Create your views here.
def homePageView(request):  #new
    return HttpResponse("Hello World")  #new