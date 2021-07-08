from django.urls import path
from django.conf.urls import url
from .views import ProductViewSet, CategoryViewSet, SearchRangePrice
from rest_framework.routers import DefaultRouter
from rest_framework_swagger.views import get_swagger_view

router = DefaultRouter()
router.register(r'product', ProductViewSet, 'product')
router.register(r'category', CategoryViewSet, 'category')
router.register(r'search', SearchRangePrice, 'search')
urlpatterns = router.urls
