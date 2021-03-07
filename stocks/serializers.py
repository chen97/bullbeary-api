from rest_meets_djongo import serializers
from stocks.models import Stocks


class StockSerializer(serializers.DjongoModelSerializer):
    class Meta:
        model = Stocks
        fields = ('full_name',
                  'stock_price',
                  'description',
                  'published',
                  'marketcap',
                  'volume',
                  'board',
                  'sector')
