from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
def display_greetings(request):
    date = datetime.datetime.now()
    h = date.strftime("%H")
    h = int(h)
    msg = "<h2>Hello, World! "
    if h<12:
        msg += "Good Morning."
    elif h<16:
        msg += "Good Afternoon."
    elif h<22:
        msg += "Good Evening."
    else:
        msg += "Good Night."
    msg += "</h2>"
    return HttpResponse(msg)

