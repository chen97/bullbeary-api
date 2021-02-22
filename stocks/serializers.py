from rest_meets_djongo import serializers
from stocks.models import Stock

class StockSerializer(serializers.DjongoModelSerializer):
    class Meta:
        model = Stock
        fields = ('id',
                  'title',
                  'description',
                  'published')