# flake8: noqa
ATTOMV4_DOCS = """BASE URL: https://api.gateway.attomdata.com/v4/

API Documentation
The API endpoint /location/lookup accepts only two parameters name and geographyTypeAbbreviation and responds with a JSON object that includes the geoIdV4 for the requested zip code.
Parameter| Format | Required | Default Description
name | string | Yes | This is the zip code to use to find the geoIdV4
geographyTypeAbbreviation | string | Yes | Geography type abbreviation (default = ZI)

The API endpoint neighborhood/community accepts only one parameter geoIdv4 and responds with a JSON object Community profile including air quailty, climate, crime, demographics, and natural disatsers for a specific geography (geoIdV4).
Parameter| Format | Required | Default Description
geoIdv4 | string | Yes | This is the specific geography code to search

The API endpoint /location/lookup accepts only two parameters name and geographyTypeAbbreviation and responds with a JSON object that is used to identify applicable geocodes (geoIdV4)
Parameter| Format | Required | Default Description
name | string | Yes | This is the location name to search
geographyTypeAbbreviation | string | Yes | Geography type abbreviation (default = PL)

"""
