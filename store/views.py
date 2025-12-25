from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from .serializers import ProductSerializer
# Create your views here.
@api_view(['GET', 'POST'])
def product_list(request):
    if request.method == 'GET':
        product = Product.objects.select_related('collection').all()
        serializer = ProductSerializer(product, many=True, context={'request': request}) #many=True tells the serializer to expect an iterable (like a queryset) and to serialize each item within it
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        print(serializer.validated_data)
        return Response('OK')

@api_view()
def product_detail(request, id):
    product = Product.objects.get(pk=id)
    serializer = ProductSerializer(product)#this serializer will convert product object to a dictionary
    return Response(serializer.data)
@api_view()
def collection_detail(request, pk):
    return Response('Ok')