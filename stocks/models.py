from django.db import models


class Stocks(models.Model):
    id = models.IntegerField(blank=False, primary_key=True)
    description = models.CharField(max_length=200, blank=False)
    published = models.CharField(max_length=70, blank=False)
    cashtag = models.CharField(max_length=70, blank=False)
    ticker = models.CharField(max_length=10, blank=True)
    code = models.CharField(max_length=10, blank=True)
    full_name = models.CharField(max_length=70, blank=False)
    stock_price = models.FloatField(blank=False)
    volume = models.FloatField(blank=False)
    marketcap = models.FloatField(blank=False)
    board = models.CharField(max_length=50, blank=True)
    sector = models.CharField(max_length=50, blank=True)
    is_shariah = models.BooleanField(blank=False)

    def __str__(self):
        return f'{self.full_name} {self.board}'
