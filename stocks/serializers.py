from rest_meets_djongo import serializers
from stocks.models import Stocks


class StockSerializer(serializers.DjongoModelSerializer):
    class Meta:
        model = Stocks
        fields = '__all__'

# class StockPriceSerializer(serializers.DjongoModelSerializer):
#     class Meta:
#         model = Stocks
#         fields = ( 'stock_price',
#                    'ticker',
#                    'board',
#                    'code')
