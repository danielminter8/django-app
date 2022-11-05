from __future__ import annotations

from datetime import datetime

from purchase_sale_api.models import PurchaseSaleData
from purchase_sale_api.services.countrycodes import get_country_iso_codes
from purchase_sale_api.services.exchangerate import get_exchange_rate


async def processor(csv_file):

    csv_data_set = csv_file.read().decode('UTF-8')
    lines = csv_data_set.split('\n')
    csv_headings = None

    for line in lines:

        fields = line.split(',')

        if csv_headings is None:
            csv_headings = extract_headings_from_csv(fields)
            continue

        if fields[0] == '':
            continue

        data = PurchaseSaleData()

        # format and parse date
        try:
            dt = datetime.strptime(fields[0], '%Y/%m/%d')
            de = f'{dt.year}-{dt.month}-{dt.day:02}'
        except Exception as e:
            print(e)

        # set csv values on model
        data.date = de
        data.description = fields[1]
        data.country = fields[2]
        data.currency = fields[3]
        data.net = fields[4]
        data.vat = fields[5]

        # get and set country iso code
        data.country_code = get_country_iso_codes(data.country)

        # convert to euros
        cc = get_exchange_rate(data.currency, dt.year, dt.month, dt.day)
        print('converting ', data.currency, ' to Euros -->', cc)
        if cc is not None and cc != '':
            data.currency = 'EUR'
            data.net = float(data.net)/float(cc)
            data.vat = float(data.vat)/float(cc)

        data.save()

    return ''


def extract_headings_from_csv(fields):
    headings = []
    for field in fields:
        headings.append(field)
    return headings
