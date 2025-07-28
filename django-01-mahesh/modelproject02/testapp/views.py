from django.shortcuts import render
from testapp import models 
import datetime

# Create your views here.
def render_index(request):
    date = datetime.datetime.now()
    my_dict = {
        "time":date,
    }
    return render(request, "testapp/index.html", context = my_dict)


def render_emp_details(request):
    emp_list = models.Employee.objects.all()
    my_dict = {
        "emp_list":emp_list
    }
    return render(request, 'testapp/emp.html', context=my_dict)