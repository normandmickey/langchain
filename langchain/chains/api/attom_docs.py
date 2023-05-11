# flake8: noqa
ATTOM_DOCS = """API documentation:
Endpoint: https://api.gateway.attomdata.com/propertyapi/v1.0.0/

Use the /property/basicprofile resource to get basic property information and most recent transaction and taxes for a specific address.

Request parameters

    address1 | string | The properties full street address including house number street name and apartment or unit number. 
    address2 | string | The city, state, zip part of the property address.
    
End of request parameters. Do not add any exclusions. 


The Response JSON object contains an three object arrays. The first is object array is labeled "status" and the second object array labled "echoed_fields" and
the third object array is labeled "property".
Following is an example response. Use example key pairs to construct an appropriate response to the question. 

{
  "status": {
    "version": "1.0.0",
    "code": 0,
    "msg": "SuccessWithResult",
    "total": 1,
    "page": 1,
    "pagesize": 10,
    "transactionID": "6a57c37e6265a6ed7f2e660040e1549f"
  },
  "echoed_fields": {
    "jobID": "",
    "loanNumber": "",
    "preparedBy": "",
    "resellerID": "",
    "preparedFor": ""
  },
  "property": [
    {
      "identifier": {
        "Id": 169970760,
        "fips": "36101",
        "apn": "463201 197.15-03-061.000",
        "attomId": 169970760
      },
      "lot": {
        "depth": 132,
        "frontage": 66,
        "lotNum": "61.000",
        "lotSize1": 0.2,
        "lotSize2": 8712,
        "zoningType": "Residential"
      },
      "area": {
        "countrySecSubd": "Steuben",
        "censusTractIdent": "961900",
        "censusBlockGroup": "4"
      },
      "address": {
        "country": "US",
        "countrySubd": "NY",
        "line1": "62 MAPLE ST",
        "line2": "CANISTEO, NY 14823",
        "locality": "CANISTEO",
        "matchCode": "ExaStr",
        "oneLine": "62 MAPLE ST, CANISTEO, NY 14823",
        "postal1": "14823",
        "postal2": "1364",
        "postal3": "C002"
      },
      "location": {
        "accuracy": "Rooftop",
        "latitude": "42.264214",
        "longitude": "-77.608617",
        "distance": 0,
        "geoid": "CO36101, CS3612265, DB3600124, PL3612254, SB0000104842, SB0000104843, ZI14823",
        "geoIdV4": {
          "CO": "8b167eca12651566bf86f0ba9720ed8a",
          "CS": "1b2f7574923e9676b5382fbce32933ad",
          "DB": "9fbcb427730003b605f2c2ae1fb37561",
          "PL": "0b42dec58134c2c0c2f135f87c6d0ebe",
          "SB": "44fb1a2bc1d4096950f0fb8f82e38bf6,6869eb0bd71a3375479dc1f89646dd5e",
          "ZI": "e388547d1ff0b5914a3c98e2af2a8bdb"
        }
      },
      "summary": {
        "absenteeInd": "OWNER OCCUPIED",
        "propClass": "Duplex, Triplex, Quadplex",
        "propSubType": "Residential",
        "propType": "DUPLEX",
        "yearBuilt": 1880,
        "propLandUse": "DUPLEX",
        "propIndicator": 21,
        "legal1": "LOT:61.000 BLK:3 SEC:197.15 DIST:463201 CITY/MUNI/TWP:CANISTEO",
        "dateOfLastQuitClaim": "04/22/2021 00:00:00"
      },
      "utilities": {
        "energyType": "YES",
        "heatingFuel": "GAS",
        "heatingType": "HOT WATER",
        "sewerType": "MUNICIPAL",
        "wallType": "ALUMINUM/VINYL"
      },
      "sale": {
        "saleSearchDate": "2021-04-22",
        "saleTransDate": "2021-04-14",
        "transactionIdent": "961143310",
        "saleAmountData": {
          "saleRecDate": "2021-04-22",
          "saleDisclosureType": 0,
          "saleDocNum": "2885/280",
          "saleTransType": "Nominal/Quit Claim"
        }
      },
      "building": {
        "size": {
          "bldgSize": 2048,
          "grossSizeAdjusted": 2048,
          "groundFloorSize": 1216,
          "livingSize": 2048,
          "sizeInd": "LIVING SQFT",
          "universalSize": 2048
        },
        "rooms": {
          "bathsFull": 2,
          "bathsTotal": 2,
          "beds": 4,
          "roomsTotal": 10
        },
        "interior": {},
        "construction": {
          "condition": "AVERAGE",
          "foundationType": "RAISED"
        },
        "parking": {
          "garageType": "Garage, Attached",
          "prkgSize": 72,
          "prkgType": "Garage, Attached"
        },
        "summary": {
          "levels": 2,
          "view": "VIEW - NONE",
          "viewCode": "000"
        }
      },
      "assessment": {
        "appraised": {},
        "assessed": {
          "assdImprValue": 52000,
          "assdLandValue": 8000,
          "assdTtlValue": 60000
        },
        "market": {
          "mktImprValue": 52000,
          "mktLandValue": 8000,
          "mktTtlValue": 60000
        },
        "tax": {
          "taxAmt": 1271.83,
          "taxPerSizeUnit": 0.62,
          "taxYear": 2021,
          "exemption": {},
          "exemptiontype": {
            "Homeowner": "Y"
          }
        },
        "improvementPercent": 86,
        "owner": {
          "corporateIndicator": "Y",
          "owner1": {
            "lastName": "NORMAN J MOORE LIVING TRUST "
          },
          "owner2": {},
          "owner3": {},
          "owner4": {},
          "absenteeOwnerStatus": "O",
          "mailingAddressOneLine": "62 MAPLE ST, CANISTEO, NY 14823-1364"
        },
        "mortgage": {
          "FirstConcurrent": {
            "amount": 0
          },
          "SecondConcurrent": {
            "amount": 0
          }
        }
      },
      "vintage": {
        "lastModified": "2023-03-21",
        "pubDate": "2023-03-21"
      }
    }
  ]
}

"""
