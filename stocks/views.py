from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from stocks.models import Stocks
from stocks.serializers import StockSerializer

from rest_framework.decorators import api_view

@api_view(['GET', 'POST', 'DELETE'])
def stock_list(request):
    if request.method == 'GET':
        stocks = Stocks.objects.all()
        
        title = request.GET.get('title', None)
        if title is not None:
            stocks = stocks.filter(title__icontains=title)
        
        stocks_serializer = StockSerializer(stocks, many=True)
        return JsonResponse(stocks_serializer.data, safe=False)
        # 'safe=False' for objects serialization
 
    elif request.method == 'POST':
        stock_data = JSONParser().parse(request)
        stock_serializer = StockSerializer(data=stock_data)
        if stock_serializer.is_valid():
            stock_serializer.save()
            return JsonResponse(stock_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(stock_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Stocks.objects.all().delete()
        return JsonResponse({'message': '{} Tutorials were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
 