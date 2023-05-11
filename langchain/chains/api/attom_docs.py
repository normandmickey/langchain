# flake8: noqa
ATTOM_DOCS = """BASE URL: https://api.gateway.attomdata.com/propertyapi/v1.0.0/

API Documentation
The API endpoint /property/basicprofile accepts only two parameters address1 and address2 and responds with a JSON object that contains basic property information. 

Parameter| Format | Required | Default Description
address1 | string | Yes | The properties full street address including house number street name and apartment or unit number. 
address2 | string | Yes | The city, state part of the property address.

Response schema (JSON object):
status | object | status
echoed_fields | object | echoed fields
property | object | property details

Each object in the property object contains the following key pairs.
key | value | description
owner1 | string | proerty owners name
yearBuilt | string | year the property was built

"""
