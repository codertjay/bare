from django.db import models

# Create your models here.
class Stock(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    timestamp = models.DateField( auto_now_add=True)
    last_update = models.DateField(  auto_now_add=True)
