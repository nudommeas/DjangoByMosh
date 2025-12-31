from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from .filter import ProductFilter   
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet, GenericViewSet
from .models import Product, Collection, Review, Cart
from .serializers import ProductSerializer, CollectionSerializer, ReviewSerializer, CartSerializer
from django.db.models import Count
from .pagination import DefualtPagination
# Create your views here.

class ProductViewset(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = ProductFilter
    pagination_class = DefualtPagination
    search_fields = ['title', 'description']
    ordering_fields = ['unit_price', 'last_update']


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
    
class CartViewSet(CreateModelMixin, GenericViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    