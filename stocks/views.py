from django.http.response import JsonResponse
# from rest_framework.parsers import JSONParser
# from rest_framework import status
from stocks.models import Stocks
from stocks.serializers import StockSerializer
from django.views.decorators.http import require_GET


@require_GET
def GetStocksFromBoard(request, board):
    q = Stocks.objects.filter(board=board)
    s = StockSerializer(q, many=True)
    return JsonResponse(s.data, safe=False)


@require_GET
def GetStockDetails(request, board, code):
    q = Stocks.objects.filter(code=code).filter(board=board)
    s = StockSerializer(q, many=True)
    return JsonResponse(s.data, safe=False)
