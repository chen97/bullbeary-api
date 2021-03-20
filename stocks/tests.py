from django.test import TestCase, RequestFactory
from django.contrib.auth.models import AnonymousUser
from .models import Stocks
from .views import StockDetails
# python manage.py test stocks


class StocksModelTests(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.user = AnonymousUser()
        # Creating Multiple Test Objects
        Stocks.objects.create(id=1, description="This is a test", published="Yes",
                              cashtag="Test", ticker="DNEX", code="4456", full_name="Dagang Exchange", stock_price=0.55, volume=5 * 10**7, marketcap=(1.5*10**9), board="KLSE", sector="O&G", is_shariah=True)
        Stocks.objects.create(id=2, description="This is a test", published="Yes",
                              cashtag="Test", full_name="XiaoMi", ticker="MI", code="1810", stock_price=0.75, volume=5 * 10**7, marketcap=(1.5*10**9), board="HKEX", sector="Technology", is_shariah=True)
        Stocks.objects.create(id=3, description="This is a test", published="Yes",
                              cashtag="Test", ticker="PETDAG", code="5681", full_name="PETRONAS Dagangan Berhad", stock_price=1.1, volume=5 * 10**4, marketcap=(1.5*10**9), board="KLSE", sector="O&G", is_shariah=True)

    # Test Model
    # def test_findExistingStock(self):

    #     stock = Stocks.objects.get(code="4456")
    #     self.assertEqual(stock.full_name, "Dagang Exchange")

    # def test_findDoesNotExistStock(self):

    #     invalidStock = None
    #     try:
    #         invalidStock = Stocks.objects.get(ticker="NotExist")
    #     except Stocks.DoesNotExist:
    #         invalidStock = "DNE"
    #     self.assertEqual(invalidStock, "DNE")

    # def test_findStocksWithPriceGreaterThan(self):

    #     q = Stocks.objects.filter(stock_price__gte=0.6)
    #     self.assertEqual(len(q), 2)

    # Test  API
    def test_get_StockDetails(self):
        request = self.factory.get(
            '/api/stocks/KLSE/4456')
        request.user = self.user

        test_kwargs = {'board': 'KLSE', 'code': '4456'}
        view = StockDetails()
        # view.kwargs = test_kwargs
        print(view)
        response = view.as_view()(request)
        # print(response)
        self.assertEqual(response.status_code, 200)
