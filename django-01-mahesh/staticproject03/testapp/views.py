from django.shortcuts import render

# Create your views here.
def indexpage(requrest):
    return render(requrest, 'testapp/index.html')

def display_pooja(request):
    return render(request, 'testapp/pooja.html')

def display_samantha(request):
    return render(request, 'testapp/samantha.html')

def display_tamanna(request):
    return render(request, 'testapp/tamanna.html')