from django.shortcuts import render

# Create your views here.
def render_index(request):
    return render(request, 'testapp/index.html')

def render_pooja_page(request):
    name = "pooja"
    my_dict = {
        "name":name,
    }
    return render(request, 'testapp/heroine.html',context=my_dict)

def render_samantha_page(request):
    name = "samantha"
    my_dict = {
        "name":name,
    }
    return render(request, 'testapp/heroine.html', context=my_dict)

def render_tamanna_page(request):
    name = "tamanna"
    my_dict = {
        "name":name,
    }
    return render(request, 'testapp/heroine.html', context=my_dict)