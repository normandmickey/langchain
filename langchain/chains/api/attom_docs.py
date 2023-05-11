# flake8: noqa
ATTOM_DOCS = """API documentation:
Endpoint: https://api.gateway.attomdata.com/propertyapi/v1.0.0/

Use the /property/basicprofile resource to get basic property information and most recent transaction and taxes for a specific address.

There are only two request parameters in addition to the header.

    address1 | string | The properties full street address including house number street name and apartment or unit number. 
    address2 | string | The city, state part of the property address.
    
The Response JSON object contains an three object arrays. The first is object array is labeled "status" and the second object array labled "echoed_fields" and
the third object array is labeled "property".
Create and run the API call based on the address in the question to parse the resulting JSON objects and key pairs to find return the answer.  
Here are some examples of the API calls to generate.

1. When was "62 Maple St, Canisteo NY" built? The API call would be 
https://api.gateway.attomdata.com/propertyapi/v1.0.0/property/basicprofile?address1=62%20Maple%20St&address2=Canisteo%20NY

2. Who owns the house located at "12 E Academy St, Canisteo NY"? The API call would be 
https://api.gateway.attomdata.com/propertyapi/v1.0.0/property/basicprofile?address1=12%20E%20Academy%20St&address2=Canisteo%20NY


"""
