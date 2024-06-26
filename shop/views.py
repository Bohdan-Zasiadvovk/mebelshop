from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    context = dict = {
        'title': 'Home',
        'content': 'HOME PAGE blablabla'
    }
    return render(request, 'shop/index.html', context)

def about(request):
    return HttpResponse("About me!")
