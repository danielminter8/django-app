from django.db import models


class PurchaseSaleData(models.Model):

    date = models.DateField()
    country = models.TextField(blank=False, default='')
    country_code = models.TextField(max_length=3, blank=False, default='')
    description = models.TextField(blank=False, default='')
    currency = models.TextField(max_length=3, blank=False, default='')
    net = models.FloatField()
    vat = models.FloatField()
