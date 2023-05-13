# flake8: noqa
ATTOMV4_DOCS = """BASE URL: https://api.gateway.attomdata.com/v4/

API Documentation
The API endpoint /location/lookup accepts only two parameters name and geographyTypeAbbreviation and responds with a JSON object that is used to identify applicable geocodes (geoIdV4)
Parameter| Format | Required | Default Description
name | string | Yes | This is the location name to search
geographyTypeAbbreviation | string | Yes | Geography type abbreviation (default = PL)

The API endpoint neighborhood/community accepts only one parameter geoIdv4 and responds with a JSON object Community profile including air quailty, climate, crime, demographics, and natural disatsers for a specific geography (geoIdV4).
Parameter| Format | Required | Default Description
geoIdv4 | string | Yes | This is the specific geography code to search

The API endpoint /location/lookup accepts only two parameters name and geographyTypeAbbreviation and responds with a JSON object that is used to identify applicable geocodes (geoIdV4)
Parameter| Format | Required | Default Description
name | string | Yes | This is the location name to search
geographyTypeAbbreviation | string | Yes | Geography type abbreviation (default = PL)

The API endpoint transaction/salestrend accepts only three parameters geoIdv4, startyear, endyear and interval and responds with a JSON object Get the average sale price, median sale price, and count of sales for the past 5 years in yearly intervals..
Parameter| Format | Required | Default Description
geoIdv4 | string | Yes | This is the specific geography code to search
startyear | integer | Yes | The start year to search from
endyear | integer | Yes | The end year to search from
interval | string | Yes | The interval to search from (valid intervals are yearly, monthly and quarterly).

"""
