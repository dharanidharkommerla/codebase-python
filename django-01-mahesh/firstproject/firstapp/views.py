from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def display(request):
    msg = "<h2>Hello, World!</h2>"
    return HttpResponse(msg)
