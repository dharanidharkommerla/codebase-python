from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def exam_view(request):
    return HttpResponse('<h2>Exam View</h2>')

def attendance_view(request):
    return HttpResponse('<h2>Attendance View</h2>')

def fee_view(request):
    return HttpResponse('<h2>Fee View</h2>')