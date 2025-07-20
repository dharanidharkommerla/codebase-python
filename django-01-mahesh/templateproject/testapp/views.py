from django.shortcuts import render
import datetime

# Create your views here.
def wish(request):
    date = datetime.datetime.now()
    msg = "Hello, World! Very Good "
    h = int(date.strftime('%H'))
    if h<12:
        msg += 'Morning'
    elif h<16:
        msg += 'Afternoon'
    elif h<21:
        msg += 'Evening'
    else:
        msg += 'Night'

    # dictionary
    student_details = {
        "name" : "sunny",
        "rollno" : 101,
        "marks" : 99
    }
    my_dict = {
        'fulldatetime': date,
        'msg':msg,
        'name':student_details['name'],
        'rollno':student_details['rollno'],
        'marks':student_details['marks'],
    }
    return render(request, 'testapp/wish.html', context=my_dict)
    # return render(request, 'testapp/wish.html', my_dict)
    # return render(request, 'testapp/wish.html', {'insert_time': date,})
