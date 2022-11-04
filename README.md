# Simple Django API

This Django project contains one app, that's a rest api that ingests uploaded csv data and santizes, processes and stores data to db.

## Goals of project
To upload purchase sale csv data, and convert all currency values to Euros according to the exchange at the time the entry was created as well as getting ISO 3166 for each country.

## Features
- Ingest purchase sale CSV data
- Get currency in Euro's at specific time of data entry
- Get ISO 3166 country code for each country
- List stored data by specified country and date

## Steps to run

<!-- - Run via Docker with a postgres db
```
docker-compose up
``` -->

- Run without Docker
```
sh run.sh
```

## Still to do features
- Some data still not sanitized
- Run in Docker(some minor issue) along with connecting to postgres db
- Upload CSV data asynchronously
- Make upload of CSV data dynamic, so if more columns/headings is added or rerrranged it won't break the code
- Refactor and folder restructure
- Make use of database read only replicas
- Basic auth e.g api_key

## Available commands
- ```sh clean.sh```


### Data sources
[ECB SDMX 2.1 RESTful]("https://sdw-wsrest.ecb.europa.eu/help/") <br/>
[Datahub Country Lists](https://pkgstore.datahub.io/core/country-list/data_json/data/8c458f2d15d9f2119654b29ede6e45b8/data_json.json)