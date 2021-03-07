from django.test import TestCase
from .models import Stocks

# Create your tests here.


class StocksModelTests(TestCase):

    def setUp(self):
        Stocks.objects.create(id=1, description="This is a test", published="Yes",
                              cashtag="Test", name="Dnex1", full_name="Dagang Exchange1", stock_price=0.55, volume=5 * 10**7, marketcap=(1.5*10**9), board="KLSE", sector="O&G", is_shariah=True)
        Stocks.objects.create(id=2, description="This is a test", published="Yes",
                              cashtag="Test", name="Dnex2", full_name="Dagang Exchange2", stock_price=0.75, volume=5 * 10**7, marketcap=(1.5*10**9), board="KLSE", sector="O&G", is_shariah=True)
        Stocks.objects.create(id=3, description="This is a test", published="Yes",
                              cashtag="Test", name="Dnex3", full_name="Dagang Exchange3", stock_price=1.1, volume=5 * 10**4, marketcap=(1.5*10**9), board="KLSE", sector="O&G", is_shariah=True)

    def test_findExistingStock(self):

        stock = Stocks.objects.get(name="Dnex3")
        self.assertEqual(stock.full_name, "Dagang Exchange3")

    def test_findDoesNotExistStock(self):

        invalidStock = None
        try:
            invalidStock = Stocks.objects.get(name="NotExist")
        except Stocks.DoesNotExist:
            invalidStock = "DNE"
        self.assertEqual(invalidStock, "DNE")

    def test_findStocksWithPriceGreaterThan(self):

        q = Stocks.objects.filter(stock_price__gte=0.6)
        # print(q)
        self.assertEqual(len(q), 2)
