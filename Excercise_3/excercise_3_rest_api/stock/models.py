from django.db import models

# Create your models here.
class Stock(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField()
    created_date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
