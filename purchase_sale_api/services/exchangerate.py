import requests


def get_exchange_rate(currency, year, month, day):

    if month < 10:
        month = "0" + str(month)
    if day < 10:
        day = "0" + str(day)
    date = str(year) + "-" + str(month) + "-" + str(day)

    url = "https://sdw-wsrest.ecb.europa.eu/service/data/EXR/D.{}.EUR.SP00.A?format=jsondata&lastNObservations=1&startPeriod={}".format(
        currency, date)
    r = requests.get(url)
    r.headers['Accept'] = 'application/json'
    r.headers['content-type'] = 'application/json; charset=utf8'

    try:
        repsonse = r.json()
        if r.status_code != 200:
            return ""
        dataset = repsonse["dataSets"][0]
        observations = dataset["series"]["0:0:0:0:0"]["observations"]
        conversion_value = observations["0"][0]
        return conversion_value
    except Exception as e:
        print("could not get currency exchange rate.")

    return ""
