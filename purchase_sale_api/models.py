from django.db import models
import json

class PurchaseSaleData(models.Model):
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
        sort_keys=True, indent=4)

    date = models.DateField()
    country = models.TextField(blank=False, default='')
    country_code = models.TextField(max_length=3, blank=False, default='')
    description = models.TextField(blank=False, default='')
    currency = models.TextField(max_length=3, blank=False, default='')
    net = models.FloatField()
    vat = models.FloatField()