from django.db.models import Model, IntegerField, FloatField, CharField, BooleanField


class Stocks(Model):
    id = IntegerField(blank=False, primary_key=True)
    description = CharField(max_length=200, blank=False)
    published = CharField(max_length=70, blank=False)
    cashtag = CharField(max_length=70, blank=False)
    ticker = CharField(max_length=10, blank=True)
    code = CharField(max_length=10, blank=True)
    full_name = CharField(max_length=70, blank=False)
    stock_price = FloatField(blank=False)
    volume = FloatField(blank=False)
    marketcap = FloatField(blank=False)
    board = CharField(max_length=50, blank=True)
    sector = CharField(max_length=50, blank=True)
    is_shariah = BooleanField(blank=False)

    def __str__(self):
        return f'{self.full_name} {self.board}'
