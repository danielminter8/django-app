import requests

countries = None


def get_country_iso_codes(country):

    global countries

    if countries is None:
        print("one time req to get all countries iso codes")
        url = 'https://pkgstore.datahub.io/core/country-list/data_json/data/8c458f2d15d9f2119654b29ede6e45b8/data_json.json'
        r = requests.get(url)
        response = r.json()
        countries = response

    for code in countries:
        if code["Name"] == country:
            return code["Code"]

    return country
