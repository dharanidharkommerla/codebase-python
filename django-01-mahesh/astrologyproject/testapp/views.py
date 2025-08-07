from django.shortcuts import render
import datetime
import random
# Create your views here.

def result_view(request):
    time = datetime.datetime.now()
    names_list = ['sunny','katrina','kareena','deepika','mallika','alia']
    msg_list = [
        'The golden days are ahead',
        'Better to sleep more time in class',
        'Tomorrow is the perfect to propose to your gf',
        'ver soon you will get a better job',
        'very soon u will get Marriage',
    ]
    h = int(time.strftime('%H'))
    if h<12:
        s = 'Good Morining'
    elif h<16:
        s  = 'Good Afternoon'
    elif h<21:
        s = 'Good Evening'
    else:
        s = 'Good Night'
    name = random.choice(names_list)
    msg = random.choice(msg_list)
    my_dict = {
        'time':time,
        'name':name,
        'msg':msg,
        'wish':s,
    }
    return render(request,"testapp/astrology.html",context=my_dict)