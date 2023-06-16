from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import permissions
from store.models import Product
from .serializers import ProductSerializer
from django.shortcuts import render
from .permissions import IsAuthorOrReadOnly


class ProductAPIView(ListAPIView):
    # permission_classes = (IsAuthorOrReadOnly,)
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetailAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly, )
    queryset = Product.objects.all()
    serializer_class = ProductSerializer



    # def get_queryset(self):
    #     queryset = Product.objects.all()
    #     name = self.request.query_params.get('name')
    #     if name is not None:
    #         queryset = queryset.filter(name__icontains=name)
    #     return queryset
    
    # def get(self, request, *args, **kwargs):
    #     print(request.query_params, 'ishladi')
    #     return super().get(request, *args, **kwargs)
    
# Create your views here.
