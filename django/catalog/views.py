from django.shortcuts import render

# Create your views here.


def index(request):
    context = {
        'message':  "This site is really about the REST API.  Maybe you should look there"
    }
    return render(request, 'catalog/index.html', context)
