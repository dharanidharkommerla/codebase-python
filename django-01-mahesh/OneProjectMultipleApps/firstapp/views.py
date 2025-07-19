from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def wish1(request):
    return HttpResponse('<h1>Message is from First Application. It is too good!!!</h1>')

