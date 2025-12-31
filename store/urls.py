from django.urls import path
# from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers
from . import views
# from pprint import pprint

router = routers.DefaultRouter()
router.register(r'products', views.ProductViewset, basename='products')
router.register(r'collections', views.CollectionViewset)
router.register(r'carts', views.CartViewSet)

product_router = routers.NestedDefaultRouter(router, 'products', lookup='product') #We're going to have a parameter called product_pk
product_router.register('reviews', views.ReviewViewSet, basename='product-review') # used as a prefix for generating the name of URL pattern

urlpatterns = router.urls + product_router.urls # store/products/{products_pk}/reviews/{pk}