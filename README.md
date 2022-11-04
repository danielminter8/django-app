# Simple Django API

This Django project contains one app, that's a rest api that ingests uploaded csv data and santizes, processes and stores data to db.

## Goals of project
To upload purchase sale csv data, and convert all currency values to Euros according to the exchange at the time the entry was created as well as getting ISO 3166 for each country. Followed by the ability to filter through the data via a get endpoint.

## Features
- Ingest purchase sale CSV data.
- Standardize currency values to Euros based on the exchange at the time.
- Get and store ISO 3166 country code for each country.
- Filter through stored data by specified country ISO code and date.

## Project structure

```
├── core/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── purchase_sale_api/
│   ├── migrations/
│   ├── services/
│   ├── utils/
│   ├── urls.py
│   ├── apps.py
│   └── ...
├── .gitignore
├── clean.sh
├── db.sqlite3 # present after migrations run
├── docker-compose.yml
├── Dockerfile
├── example.csv
├── manage.py
├── README.md
├── requirements.txt
└── run.sh
```

## Steps to run

<!-- - Run via Docker with a postgres db
```
docker-compose up
``` -->

- Run without Docker
```
sh run.sh
```

## API usage

| Method | Endpoint                                                 | Usage                                                                                                                               |
|--------|----------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| GET    | http://localhost:8080/                                   | Server liveness check, just returns 200Ok if server is up.                                                                          |
| POST   | http://localhost:8080/upload                             | Upload CSV as a form data body type with a key of 'file'.                                                                           |
| GET    | http://localhost:8080/data?country={country}&date={date} | Query params need to be specified, 'country' needs to be an ISO 3166 code e.g ```ZA``` and date needs to be in this format ```2022-04-28```. |

## Still to do
- [] Some data still not sanitized
- [] Run in Docker(some minor issue) along with connecting to postgres db
- [] Upload CSV data asynchronously
- [] Make upload of CSV data dynamic, so if more columns/headings is added or rerrranged it won't break the code
- [] Refactor and folder restructure
- [] Make use of database read only replicas
- [] Basic auth e.g api_key

## Available commands
- ```sh clean.sh```


### Data sources
[ECB SDMX 2.1 RESTful](https://sdw-wsrest.ecb.europa.eu/help/)\
[Datahub Country Lists](https://pkgstore.datahub.io/core/country-list/data_json/data/8c458f2d15d9f2119654b29ede6e45b8/data_json.json)