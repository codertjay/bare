from .models import Stock
from rest_framework.serializers import ModelSerializer

class StockSerializer(ModelSerializer):
    class Meta:
        model = Stock
        fields = '_all__'


    def update(self, instance, validated_data):
        # MANIPULATE DATA HERE BEFORE INSERTION

        instance = super(ProduitUpdateSerializer,self).update(instance, validated_data)
        # ADD CODE HERE THAT YOU WANT TO VIEW
        instance.last_update = datetime.now()
        instance.save()
        return instance

