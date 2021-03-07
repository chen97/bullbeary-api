# from django.conf.urls import url
from django.urls import path
from stocks.views import GetStockDetails, GetStocksFromBoard

urlpatterns = [
    path('<board>', GetStocksFromBoard),
    path('<board>/<code>', GetStockDetails)
]
