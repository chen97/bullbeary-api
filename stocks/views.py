from django.http.response import JsonResponse
# from rest_framework.parsers import JSONParser
# from rest_framework import status
from stocks.models import Stocks
from stocks.serializers import StockSerializer
from rest_framework import generics
from django.views.decorators.http import require_safe

# Web servers should automatically strip the content of responses to HEAD requests while leaving the headers unchanged,
# so you may handle HEAD requests exactly like GET requests in your views. Since some software,
# such as link checkers, rely on HEAD requests, you might prefer using require_safe instead of require_GET.


# @require_safe
# def GetStockDetails(request, board, code):
#     q = Stocks.objects.filter(code=code).filter(board=board)
#     s = StockSerializer(q, many=True)
#     return JsonResponse(s.data, safe=False)


# @require_safe
# def GetStocksFromBoard(request, board):
#     q = Stocks.objects.filter(board=board)
#     s = StockSerializer(q, many=True)
#     return JsonResponse(s.data, safe=False)


class StockListsFromBoard(generics.ListAPIView):
    serializer_class = StockSerializer
    permission_classes = []

    def get_queryset(self):
        board = self.kwargs['board']
        return Stocks.objects.filter(board=board)

    def get(self, request, board):

        serializer = self.get_serializer(self.get_queryset(), many=True)
        return JsonResponse(serializer.data, safe=False)


class StockDetails(generics.ListAPIView):
    serializer_class = StockSerializer
    permission_classes = []

    def get_queryset(self):
        board = self.kwargs['board']
        code = self.kwargs['code']
        return Stocks.objects.filter(board=board, code=code)

    def get(self, request, board, code):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return JsonResponse(serializer.data, safe=False)
