# flake8: noqa
ATTOM_DOCS = """BASE URL: https://api.gateway.attomdata.com/propertyapi/v1.0.0/

API Documentation
The API endpoint /property/basicprofile accepts only two parameters address1 and address2 and responds with a JSON object that contains basic property information. 
Parameter| Format | Required | Default Description
address1 | string | Yes | The properties full street address including house number street name and apartment or unit number. 
address2 | string | Yes | The city, state part of the property address.

Reponse key pairs
key | format | description
absenteeInd | string | absentee indicator
propClass | string | property class
propSubType | string | property subtype
propType | string | property type
yearBuilt| year build | year built
propLandUse | string | land use
propIndicator stirng | property indicator
legal1 | string | legal id
dateOfLastQuitClaim | date | date of last quit claim
energyType | string | energy type
heatingFuel | string | heating fuel
heatingType | string | heating type
sewerType | string | sewar type
wallType | string | wall type

The API endpoint /property/address accepts five parameters postalcode, propertytype, orderby, page, pagesize and responds with a JSON object that contains a list of properties within a zip code.
Paramer| Format | Required | Default Description
postalcode | string | Yes | The zip code or posstal code to search.
propertytype | string | Yes | A specific property classification such as 'Detached Single Family'
orderby | string | Yes | 	Sorting Options
page | integer | Yes | 	The current view index based on the pagesize and the total number of records available
pagesize | integer | Yes | The number of records to be returned with the request

"""
