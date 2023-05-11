# flake8: noqa
ATTOM_DOCS = """API documentation:
Endpoint: https://api.gateway.attomdata.com/propertyapi/v1.0.0/

Use the /property/address resource to get list of properties within a zip code.

Request parameters

    postalcode | string | The zip code or postal code to search
    properytype | string | 	A specific property classification such as 'Detached Single Family'
    orderby | string | Sorting Options
    page | string | The current view index based on the pagesize and the total number of records available
    pagesize | string | The number of records to be returned with the request


The Response JSON object contains an two object arrays. The first is object array is labeled "status" and the second object array labled "property".
Following is an example response. Use example key pairs to construct an appropriate response to the question. 

Response Body
{
  "status": {
    "version": "1.0.0",
    "code": 0,
    "msg": "SuccessWithResult",
    "total": 10000,
    "page": 1,
    "pagesize": 5,
    "transactionID": "d2f3ba1c34c30efb4ad5df672a27ffbb"
  },
  "property": [
    {
      "identifier": {
        "Id": 229706256,
        "fips": "56021",
        "apn": "43281007300000",
        "attomId": 229706256
      },
      "address": {
        "country": "US",
        "countrySubd": "WY",
        "line1": "2862 BAREBACK BLVD",
        "line2": "CHEYENNE, WY 82009",
        "locality": "CHEYENNE",
        "matchCode": "ExaStr",
        "oneLine": "2862 BAREBACK BLVD, CHEYENNE, WY 82009",
        "postal1": "82009",
        "postal2": "7440"
      },
      "location": {
        "accuracy": "Rooftop",
        "latitude": "41.413640",
        "longitude": "-104.544461",
        "distance": 0,
        "geoid": "CO56021, CS5690715, DB5601980, PL5613900, RS0005163012, SB0000130742, SB0000130746, SB0000130770, ZI82009",
        "geoIdV4": {
          "CO": "16856031afb1b236f0d628bb802eac71",
          "CS": "e5a490a174895893b11ce251b6cea7bd",
          "DB": "898d6145ddc5cc2da48b3a7457b73aa0",
          "N4": "50624bbc081fdfff4febc9c3c8eba234",
          "SB": "df75b4c66b67b3621a83f75724addf21,7ac7c644bb9caea592cd40b7008a0f42,2783806e402d9117e4e7e37451646b56,2d009e71f6fbc08892495abe6d6592c2,0ffa3c3db0f6bb9a8ee73eaea0e51e89",
          "ZI": "ac6c213665a7701bd3617ada1ff96513"
        }
      },
      "vintage": {
        "lastModified": "2023-05-03",
        "pubDate": "2023-05-03"
      }
    },
    {
      "identifier": {
        "Id": 241066404,
        "fips": "56021",
        "apn": "18300007100000",
        "attomId": 241066404
      },
      "address": {
        "country": "US",
        "countrySubd": "WY",
        "line1": "1777 E MULE TRL",
        "line2": "CHEYENNE, WY 82009",
        "locality": "CHEYENNE",
        "matchCode": "ExaStr",
        "oneLine": "1777 E MULE TRL, CHEYENNE, WY 82009",
        "postal1": "82009",
        "postal2": "8314"
      },
      "location": {
        "accuracy": "Rooftop",
        "latitude": "41.259383",
        "longitude": "-105.079029",
        "distance": 0,
        "geoid": "CO56021, CS5690825, DB5601980, SB0000130742, SB0000130746, SB0000130762, ZI82009",
        "geoIdV4": {
          "CO": "16856031afb1b236f0d628bb802eac71",
          "CS": "afb4f4d8de38f997097b0e3a2e7f8081",
          "DB": "30c86a3f2f5c848363c435461b716572",
          "N4": "e8496eabcd3c4835fd9dc6a0e9056e37",
          "SB": "d6c29ef37357615935d1950d844bf948,5052e691ea6a3cddbe9d3056b3dcf6bd,b201130baed862e8452f23b5c98506ca",
          "ZI": "ac6c213665a7701bd3617ada1ff96513"
        }
      },
      "vintage": {
        "lastModified": "2023-05-02",
        "pubDate": "2023-05-02"
      }
    },
    {
      "identifier": {
        "Id": 332526697,
        "fips": "56021",
        "apn": "19500005400000",
        "attomId": 332526697
      },
      "address": {
        "country": "US",
        "countrySubd": "WY",
        "line1": "2348 OLD FAITHFUL WAY",
        "line2": "CHEYENNE, WY 82009",
        "locality": "CHEYENNE",
        "matchCode": "ExaStr",
        "oneLine": "2348 OLD FAITHFUL WAY, CHEYENNE, WY 82009",
        "postal1": "82009",
        "postal2": "9810"
      },
      "location": {
        "accuracy": "Rooftop",
        "latitude": "41.331211",
        "longitude": "-104.837305",
        "distance": 0,
        "geoid": "CO56021, CS5690715, DB5601980, PL5613900, RS0005163012, SB0000130742, SB0000130746, SB0000130770, ZI82009",
        "geoIdV4": {
          "CO": "16856031afb1b236f0d628bb802eac71",
          "CS": "e5a490a174895893b11ce251b6cea7bd",
          "DB": "30c86a3f2f5c848363c435461b716572",
          "SB": "5052e691ea6a3cddbe9d3056b3dcf6bd,cf0fc2d50f6fdb4f2c6d6a6e127945b9,d6c29ef37357615935d1950d844bf948",
          "ZI": "ac6c213665a7701bd3617ada1ff96513"
        }
      },
      "vintage": {
        "lastModified": "2023-05-03",
        "pubDate": "2023-05-03"
      }
    },
    {
      "identifier": {
        "Id": 334396798,
        "fips": "56021",
        "apn": "19267000300160",
        "attomId": 334396798
      },
      "address": {
        "country": "US",
        "countrySubd": "WY",
        "line1": "5126 CARLA DR",
        "line2": "CHEYENNE, WY 82009",
        "locality": "CHEYENNE",
        "matchCode": "ExaZip",
        "oneLine": "5126 CARLA DR, CHEYENNE, WY 82009",
        "postal1": "82009",
        "postal2": ""
      },
      "location": {
        "accuracy": "Zip5",
        "latitude": "41.165419",
        "longitude": "-104.761977",
        "distance": 0,
        "geoid": "CO56021, CS5690715, DB5601980, PL5613900, RS0005163012, SB0000130742, SB0000130746, SB0000130770, ZI82009",
        "geoIdV4": {
          "CO": "16856031afb1b236f0d628bb802eac71"
        }
      },
      "vintage": {
        "lastModified": "2023-05-02",
        "pubDate": "2023-05-02"
      }
    },
    {
      "identifier": {
        "Id": 578088,
        "fips": "56021",
        "apn": "13146000800250",
        "attomId": 578088
      },
      "address": {
        "country": "US",
        "countrySubd": "WY",
        "line1": "3009 HOLLAND CT",
        "line2": "CHEYENNE, WY 82009",
        "locality": "CHEYENNE",
        "matchCode": "ExaStr",
        "oneLine": "3009 HOLLAND CT, CHEYENNE, WY 82009",
        "postal1": "82009",
        "postal2": "4566",
        "postal3": "C048"
      },
      "location": {
        "accuracy": "Rooftop",
        "latitude": "41.172466",
        "longitude": "-104.773287",
        "distance": 0,
        "geoid": "CO56021, CS5690715, DB5601980, PL5613900, RS0000102379, SB0000130743, SB0000130744, SB0000130770, ZI82009",
        "geoIdV4": {
          "CO": "16856031afb1b236f0d628bb802eac71",
          "CS": "29392c8fb7766fb633eb98b90048e74f",
          "DB": "30c86a3f2f5c848363c435461b716572",
          "N4": "c37899643b6f433b3d70028e8f3ff28d",
          "PL": "802b98230660b6ebebd36a06ec9e541e",
          "SB": "92f4e3680e213202ff124f1d710f43b3,72a8a2071295f29e10bf6a4009b6d030",
          "ZI": "ac6c213665a7701bd3617ada1ff96513"
        }
      },
      "vintage": {
        "lastModified": "2023-05-02",
        "pubDate": "2023-05-02"
      }
    }
  ]
}

Use the /property/basicprofile resource to get basic property information and most recent transaction and taxes for a specific address.

Request parameters

    address1 | string | The properties full street address including house number street name and apartment or unit number. 
    address2 | string | The city, state, zip part of the property address.


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
