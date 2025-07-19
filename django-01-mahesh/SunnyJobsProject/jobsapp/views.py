from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def hyd_jobs_info(request):
    s = "<h2>Hyderabad Jobs Information...</h2>"
    return HttpResponse(s)

def che_jobs_info(request):
    s = "<h2>Chennai Jobs Information...</h2>"
    return HttpResponse(s)

def ban_jobs_info(request):
    s = "<h2>Bangolre Jobs Information...</h2>"
    return HttpResponse(s)

def pun_jobs_info(request):
    s = "<h2>Pune Jobs Information...</h2>"
    return HttpResponse(s)

def mum_jobs_info(request):
    s = "<h2>Mumbai Jobs Information...</h2>"
    return HttpResponse(s)