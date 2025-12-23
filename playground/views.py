from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from store.models import Product, Collection, Order

# Create your views here.



def index(request):
    queryset = Product.objects.prefetch_related('promotion').select_related('collection')[:5]
    # queryset = Order.objects.select_related('customer').order_by('-placed_at')[:5]
    return render(request, 'hello.html', {'name': 'Nudom', 'products': list(queryset)})   