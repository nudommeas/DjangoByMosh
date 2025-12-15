from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    x = 1
    return render(request, 'hello.html', {'name': 'Nudom'})   