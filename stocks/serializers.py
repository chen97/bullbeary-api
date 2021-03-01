from rest_meets_djongo import serializers
from stocks.models import Stocks


class StockSerializer(serializers.DjongoModelSerializer):
    class Meta:
        model = Stocks
        fields = ('id',
                  'title',
                  'description',
                  'published')
