from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
def get_time(request):
    date = datetime.datetime.now()
    msg = "<h1>Hello, World!</h1>"
    msg+= f"<h2>Time is: {str(date)}</h2><hr>"
    return HttpResponse(msg)