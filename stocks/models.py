from django.db import models

class Stocks(models.Model):
    id = models.CharField(max_length=70, blank=False, primary_key=True)
    description = models.CharField(max_length=200, blank=False)
    published = models.CharField(max_length=70, blank=False)
    cashtag = models.CharField(max_length=70, blank=False)
    name = models.CharField(max_length=70, blank=False)
    full_name = models.CharField(max_length=70, blank=False)
    stock_price = models.CharField(max_length=70, blank=False)
    price_change_rm = models.CharField(max_length=70, blank=False)
    price_change_pct = models.CharField(max_length=70, blank=False)
    volume = models.CharField(max_length=70, blank=False)
    marketcap = models.CharField(max_length=70, blank=False)
    board = models.CharField(max_length=70, blank=True)
    sector = models.CharField(max_length=70, blank=True)
    is_shariah = models.CharField(max_length=70, blank=False)