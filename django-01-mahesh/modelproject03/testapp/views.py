from django.shortcuts import render
from testapp.models import Student

# Create your views here.
def render_index(request):
    return render(request, "index.html", context=None)

def render_student_details(request):
    # retrieve the data from the db
    student_list = Student.objects.all()
    mydict = {'student_list': student_list}
    return render(request, "testapp/student.html", context=mydict)
