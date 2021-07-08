from rest_framework import status
from django_filters import FilterSet
from django_filters.filters import NumberFilter, AllValuesFilter
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, ViewSet
from .serializers import ProductSerializer, CategorySerializer
from .models import Product, Category


class ProductViewSet(ModelViewSet):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    http_method_names = ['get', 'post', 'patch', 'delete']

    def list(self, request):
        products = Product.objects.filter(is_active=True)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

    def create(self, request):
        serializers = ProductSerializer(data=request.data)
        serializers.is_valid(raise_exception=True)
        serializers.save()
        return Response(serializers.data, status=status.HTTP_201_CREATED)

    def destroy(self,request, pk):
        product = Product.objects.get(id=pk)
        product.on_delete = True
        product.is_active = False
        product.save()
        serializers = ProductSerializer(product)
        return Response(serializers.data, status=status.HTTP_200_OK)


class CategoryViewSet(ModelViewSet):

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    http_method_names = ['get', 'post', 'delete']

    def create(self, request):
        serializer = CategorySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)

    def destroy(self, request, pk):
        category = Category.objects.get(id=pk)
        if category.product_set.all().count() > 0:
            return Response({'delete': "Category has product. Can't delete"}, status.HTTP_400_BAD_REQUEST)
        category.delete()
        return Response({'delete': 'success'}, status.HTTP_200_OK)


class SelfFilter(FilterSet):
        title = AllValuesFilter(field_name='title')
        title_category = AllValuesFilter(field_name='category__title')
        id_category = AllValuesFilter(field_name='category__id')
        is_active= AllValuesFilter(field_name='is_active')
        on_delete = AllValuesFilter(field_name='on_delete')
        min_price = NumberFilter(field_name='price', lookup_expr='gte')
        max_price = NumberFilter(field_name='price', lookup_expr='lte')

        class Meta:
            model = Product
            fields = ['min_price', 'max_price']

class SearchRangePrice(ListAPIView, ViewSet):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_class = SelfFilter
