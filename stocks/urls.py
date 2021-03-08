# from django.conf.urls import url
from django.urls import path
from stocks.views import StockListsFromBoard, StockDetails

urlpatterns = [
    path('<board>', StockListsFromBoard.as_view()),
    path('<board>/<code>', StockDetails.as_view())
]
