# flake8: noqa
ATTOMV4Transactions_DOCS = """BASE URL: https://api.gateway.attomdata.com/v4/

API Documentation
The API endpoint transaction/salestrend accepts only four parameters geoIdv4, startyear, endyear and interval and responds with a JSON object Get the average sale price, median sale price, and count of sales for the past 5 years in yearly intervals..
Parameter| Format | Required | Default Description
geoIdV4 | string | Yes | This is the specific geography code to search
startyear | integer | Yes | The start year to search from
endyear | integer | Yes | The end year to search from
interval | string | Yes | The interval to search from (valid intervals are yearly, monthly and quarterly).

"""
