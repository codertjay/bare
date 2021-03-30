from .models import Stock
from rest_framework.serializers import ModelSerializer
from datetime import datetime

class StockSerializer(ModelSerializer):
    class Meta:
        model = Stock
        fields = ['name','price','created_date','last_update']


    def update(self, instance, validated_data):
        # MANIPULATE DATA HERE BEFORE INSERTION

        instance = super(StockSerializer,self).update(instance, validated_data)
        # ADD CODE HERE THAT YOU WANT TO VIEW
        instance.last_update = datetime.now()
        print(instance.last_update)
        instance.save()
        return instance

