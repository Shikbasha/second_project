from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def basha(request):
    return HttpResponse('Time and Tide wait for none')
