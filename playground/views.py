from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from store.models import Product
from store.models import Collection
# Create your views here.

# __icontains 
# __contains --> lookup type
# __range --> lookup type
# __year 


def index(request):
    queryset = Product.objects.filter(Q(inventory__lt=10) & Q(unit_price__lt=20))
    return render(request, 'hello.html', {'name': 'Nudom', 'products': list(queryset)})   