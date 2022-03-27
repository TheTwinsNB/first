from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponse


# Create your views here.
def index(request):
    context = {
        'name': 'click'
    }
    # return HttpResponse('ok')
    return render(request, 'firstapp/index.html',context=context)
