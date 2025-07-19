from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def wish2(reuest):
    return HttpResponse('<h1>Message is from Second Application. It is too good!!!</h1>')