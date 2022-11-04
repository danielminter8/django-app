from purchase_sale_api.models import PurchaseSaleData
from datetime import datetime
from django.core import serializers
from purchase_sale_api.services.exchangerate import get_exchange_rate
from purchase_sale_api.services.countrycodes import get_country_iso_codes
import json


def processor(csv_file):
    csv_data_set = csv_file.read().decode('UTF-8')
    lines = csv_data_set.split("\n")
    csv_headings = None
    
    for line in lines:

        fields = line.split(",")

        if csv_headings is None:
            csv_headings = extract_headings_from_csv(fields)
            continue
            
        if fields[0] == '':
            continue

        data = PurchaseSaleData()
        try:
            dt = datetime.strptime(fields[0], '%Y/%m/%d')
            de = '{0}-{1}-{2:02}'.format(dt.year, dt.month, dt.day)
        except Exception as e:
            print(e)
        data.date = de
        data.description = fields[1]
        data.country = fields[2]
        data.currency = fields[3]
        data.net = fields[4]
        data.vat = fields[5]

        # sanitize country
        data.country_code = get_country_iso_codes(data.country)

        # convert to euros
        cc = get_exchange_rate(data.currency, dt.year, dt.month, dt.day)
        print("converting ", data.currency, " to Euros -->", cc)
        if cc is not None and cc != '':
            data.currency = "EUR"
            data.net = float(data.net)/float(cc)
            data.vat = float(data.vat)/float(cc)

  
        data.save() # save in db
    tmpJson = serializers.serialize("json", [data])
    tmpObj = json.loads(tmpJson)

    return tmpObj
    

def extract_headings_from_csv(fields):
    headings = []
    for field in fields:
        headings.append(field)
    return headings
