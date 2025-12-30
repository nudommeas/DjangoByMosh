from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from .filter import ProductFilter   
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from .models import Product, Collection, Review
from .serializers import ProductSerializer, CollectionSerializer, ReviewSerializer
from django.db.models import Count
# Create your views here.

class ProductViewset(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = ProductFilter
    search_fields = ['title', 'description']


    def get_serializer_context(self):
        return {'request': self.request}
    
    def destroy(self, request , pk):
        product = get_object_or_404(Product, pk=pk)
        product.delete()
        return Response({'message': 'The product has been removed'}, status=status.HTTP_204_NO_CONTENT)

class CollectionViewset(ModelViewSet):
    queryset = Collection.objects.annotate(products_count=Count('products')).all()
    serializer_class = CollectionSerializer

    def destroy(self, request, *args, **kwargs):
        if Product.objects.filter(collection__id=kwargs['pk']).count() > 0:
            return Response({'errors': 'Collection cannot be delete with associated product_count'})
        return super().destroy(request, *args, **kwargs)

    # def destroy(self, request, pk):
    #     collection = get_object_or_404(Collection, pk=pk)
    #     if collection.products.count() > 0:
    #         return Response({'errors': 'Collection cannot be delete with associated product_count'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
    #     collection.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)
class ReviewViewSet(ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer #In this serializer_class, we have access to the URL parameter.So we can read the product ID from the URL using a context object

    def get_queryset(self):
        # We expect a URL parameter like 'product' (defined by the router)
        # to identify the parent Product.
        product_pk = self.kwargs['product_pk']
        return Review.objects.filter(product_id=product_pk)

    def get_serializer_context(self):
        return {'product_id': self.kwargs['product_pk']}