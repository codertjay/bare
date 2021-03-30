from django.contrib.auth import get_user_model
from django.test import TestCase

from rest_framework.test import APIClient

from .models import Stock
# Create your tests here.
User = get_user_model()

class StockTestCase(TestCase):
    def setUp(self):
        Stock.objects.create(name='cfe', price=22)
        Stock.objects.create(name='cfe-2', price=223,)
       
        self.currentCount = Stock.objects.all().count()

    def get_client(self):
        client = APIClient()
        return client

    def test_stock_created(self):
        Stock_obj = Stock.objects.create(name="my second Stock", 
            price=22)
        self.assertEqual(Stock_obj.id, 3)
    
    def test_stock_list(self):
        client = self.get_client()
        response = client.get("/api/stocks/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 2)

    
    def test_stock_detail_api_view(self):
        client = self.get_client()
        response = client.get("/api/stocks/1/")
        self.assertEqual(response.status_code, 200)



    def test_stock_update(self):
        client = self.get_client()
        response = client.put('/api/stocks/2/',{'price':33,'name':'Stock changed'})
        self.assertEqual(response.status_code, 200)
