from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from store.models import Product
from store.models import Collection
# Create your views here.



def index(request):
    queryset = Product.objects.all()[:5]
    return render(request, 'hello.html', {'name': 'Nudom', 'products': list(queryset)})   