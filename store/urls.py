from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views
# from pprint import pprint

router = DefaultRouter()
router.register(r'products', views.ProductViewset)
router.register(r'collections', views.CollectionViewset)

urlpatterns = router.urls