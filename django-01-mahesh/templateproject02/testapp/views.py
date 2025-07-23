from django.shortcuts import render
import datetime
# Create your views here.
def info(request):
    date = datetime.datetime.now()
    course = "Django with Python"
    prerequisite = "Python"

    my_dict = {
        "date": date,
        "course":course,
        "prerequisite":prerequisite,
    }
    # print(my_dict)
    return render(request, "testapp/info.html",context=my_dict)