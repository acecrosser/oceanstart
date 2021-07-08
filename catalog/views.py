from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .serializers import ProductSerializer, CategorySerializer
from .models import Product, Category


class ProductViewSet(ModelViewSet):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    http_method_names = ['get', 'post', 'patch', 'delete']

    def list(self, request):
        pass

    def create(self, request):
        serializers = ProductSerializer(data=request.data)
        serializers.is_valid(raise_exception=True)
        serializers.save()
        return Response(serializers.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk):
        pass

    def destroy(self,request):
        pass


class CategoryViewSet(ModelViewSet):

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    http_method_names = ['get', 'post', 'patch', 'delete']

    def create(self, request, pk):
        pass

    def destroy(self, request, pk):
        return Response('not work now')


class SearchViewSet(ModelViewSet):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    http_method_names = ['get', ]

    def list(self, request, *args):
        pass