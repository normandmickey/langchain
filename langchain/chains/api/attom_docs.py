# flake8: noqa
ATTOM_DOCS = """BASE URL: https://api.gateway.attomdata.com/propertyapi/v1.0.0/

API Documentation
The API endpoint /property/basicprofile accepts two parameters address1 and address2 and responds with a JSON object that contains basic property information. 

Parameter| Format | Required | Default Description
address1 | string | Yes | The properties full street address including house number street name and apartment or unit number. 
address2 | string | Yes | The city, state part of the property address.

Response Object Example

    {
  "status": {
    "version": "1.0.0",
    "code": 0,
    "msg": "SuccessWithResult",
    "total": 1,
    "page": 1,
    "pagesize": 10,
    "transactionID": "560a9388fa9d78a9a64b4c3db24ce7dc"
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
        "Id": 184713191,
        "fips": "08031",
        "apn": "02192-04-018-000",
        "attomId": 184713191
      },
      "lot": {
        "lotNum": "31,32",
        "lotSize1": 0.1076676,
        "lotSize2": 4690,
        "zoningType": "Residential"
      },
      "area": {
        "countrySecSubd": "Denver",
        "subdName": "BERKELEY",
        "censusTractIdent": "102",
        "censusBlockGroup": "3"
      },
      "address": {
        "country": "US",
        "countrySubd": "CO",
        "line1": "4529 WINONA CT",
        "line2": "DENVER, CO 80212",
        "locality": "DENVER",
        "matchCode": "ExaStr",
        "oneLine": "4529 WINONA CT, DENVER, CO 80212",
        "postal1": "80212",
        "postal2": "2512",
        "postal3": "C037"
      },
      "location": {
        "accuracy": "Rooftop",
        "latitude": "39.778926",
        "longitude": "-105.047775",
        "distance": 0,
        "geoid": "CO08031, CS0891007, DB0803360, ND0000119198, ND0004861239, PL0820000, SB0000076114, SB0000076155, SB0000076161, SB0000135819, SB0000143772, ZI80212",
        "geoIdV4": {
          "CO": "1291dc1937525d78f89cebb6a43a50de",
          "CS": "4c0507d0d7894d2d48e4e03e1c0240fc",
          "DB": "d8ca7ea08abbe9efdd7e3b78f23d120e",
          "N1": "b26d02d9330761156fc0cfd4ed8bf9a1",
          "N2": "27e220314436f6edd5e606ddcd28156d",
          "PL": "7de845f7ba9b234a2c5adfca1db76c64",
          "SB": "b95eac0d6a8385db6771b9d54f2a6a1c,4287d95a26357a9a1474f9cb99e6e816,6dee2c66470af6400265dd11b87cdb7d,906cf6aada87fa5bad0a13f2f86ff5aa,b9980ca738ece2e06f9086da927317fe",
          "ZI": "0149d0a55ef2d6b71071a39f4e13d6eb"
        }
      },
      "summary": {
        "absenteeInd": "ABSENTEE(MAIL AND SITUS NOT =)",
        "propClass": "Single Family Residence / Townhouse",
        "propSubType": "Residential",
        "propType": "SFR",
        "yearBuilt": 1900,
        "propLandUse": "SFR",
        "propIndicator": 10,
        "legal1": "BERKELEY B36 L31 & S/2 OF L32 EXC REAR 8FT TO CITY"
      },
      "utilities": {
        "heatingFuel": "GAS",
        "heatingType": "CENTRAL",
        "wallType": "BRICK"
      },
      "sale": {
        "saleSearchDate": "2021-06-29",
        "saleTransDate": "2021-06-28",
        "transactionIdent": "965116373",
        "saleAmountData": {
          "saleRecDate": "2021-06-29",
          "saleDisclosureType": 0,
          "saleDocNum": "0000123161",
          "saleTransType": "Resale"
        }
      },
      "building": {
        "size": {
          "bldgSize": 934,
          "grossSize": 1414,
          "grossSizeAdjusted": 934,
          "groundFloorSize": 934,
          "livingSize": 934,
          "sizeInd": "LIVING SQFT",
          "universalSize": 934
        },
        "rooms": {
          "bathFixtures": 5,
          "bathsFull": 1,
          "bathsTotal": 1,
          "beds": 2,
          "roomsTotal": 5
        },
        "interior": {
          "bsmtSize": 480,
          "fplcCount": 1,
          "fplcInd": "Y",
          "fplcType": "YES",
          "bsmtFinishedPercent": 0
        },
        "construction": {
          "condition": "GOOD"
        },
        "parking": {
          "prkgSize": 240
        },
        "summary": {
          "levels": 1,
          "unitsCount": 1,
          "view": "VIEW - NONE",
          "viewCode": "000"
        }
      },
      "assessment": {
        "appraised": {},
        "assessed": {
          "assdImprValue": 14230,
          "assdLandValue": 22910,
          "assdTtlValue": 37140
        },
        "market": {
          "mktImprValue": 199000,
          "mktLandValue": 320400,
          "mktTtlValue": 519400
        },
        "tax": {
          "taxAmt": 2870.88,
          "taxPerSizeUnit": 3.07,
          "taxYear": 2022,
          "exemption": {},
          "exemptiontype": {}
        },
        "improvementPercent": 38,
        "owner": {
          "corporateIndicator": "Y",
          "owner1": {
            "lastName": "MATTICE, MICHAEL S LIVING TRUST "
          },
          "owner2": {},
          "owner3": {
            "lastName": "MATTICE, SHAREE LIVING TRUST "
          },
          "owner4": {},
          "absenteeOwnerStatus": "A",
          "mailingAddressOneLine": "2829 N FRANKLIN ST, DENVER, CO 80205-4510"
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
        "lastModified": "2023-02-15",
        "pubDate": "2023-02-15"
      }
    }
  ]
}
"""
