# flake8: noqa
ATTOM_DOCS = """API documentation:
Endpoint: https://api.gateway.attomdata.com/propertyapi/v1.0.0/

Use the /property/address resource to get aist of properties within a zip code.

What kinds of questions can data from the /property/address resource help answer?

Request parameters

    postalcode | string | The zip code or postal code to search
    properytype | string | 	A specific property classification such as 'Detached Single Family'
    orderby | string | Sorting Options
    page | string | The current view index based on the pagesize and the total number of records available
    pagesize | string | The number of records to be returned with the request


The Response JSON object contains an two object arrays. The first is object array is labeled "status" and the second object array labled "property". Following is an example response
use example key pairs to contstruct an appropriate response to the question. 

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
"""
