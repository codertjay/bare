from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import StockListApiView ,StockDetailUpdateApiView

app_name = 'stock'
urlpatterns = [
    path('', StockListApiView.as_view(), name='stock_list_create'),
    path('<int:pk>/',StockDetailUpdateApiView.as_view() , name='stock_detail'),
]
