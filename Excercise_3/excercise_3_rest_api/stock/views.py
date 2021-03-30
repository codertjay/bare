from django.shortcuts import render
from .serializers import StockSerializer
from .models import Stock
from rest_framework import viewsets 
from rest_framework import generics

class StockListApiView(generics.ListCreateAPIView):
    queryset= Stock.objects.all()
    serializer_class = StockSerializer

    

class StockDetailUpdateApiView(generics.RetrieveUpdateAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    lookup_field = 'pk'

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

