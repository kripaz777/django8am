from .models import *
from .serializers import *
from rest_framework import viewsets
import django_filters.rest_framework
from rest_framework import generics
from rest_framework import filters

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# ViewSets define the view behavior.
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer



class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter]
    filterset_fields = ['category', 'subcategory','stock','label']
    search_fields = ['name', 'description']
    ordering_fields = ['price', 'discounted_price','id','name']


class ProductDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = ProductSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = ProductSerializer(snippet, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
