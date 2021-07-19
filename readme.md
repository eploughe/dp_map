# Pop Mapping Utility

main.py - Utility for doing lookups and to get pop information.

usage: main.py [-h] [-l LOOKUP] [-c COUNTRY] [-i INFO] [-r REGION]

```
optional arguments:
  -h, --help            show this help message and exit
  -l LOOKUP, --lookup LOOKUP
                        Looks up primary and secondary POPs
  -c COUNTRY, --country COUNTRY
                        Lookup country code based on country name.
  -i INFO, --info INFO  Lookup POP name and ip address
  -r REGION, --region REGION
                        Lookup region data for a country/state
```

Example Lookup

```commandline
main.py -l "china"
['aphongkong', 'apnorth']
Region: aphongkong Pops:{'hkg1': 60, 'nrt1': 50}
Region: apnorth Pops:{'nrt1': 55, 'osa1': 50, 'hkg1': 40}
```

Example Country Code Lookup

```commandline
main.py -c "United Kingdom"
{"country": "United Kingdom", "code": "GB"}
```

Example POP Info Lookup

```commandline
main.py -i "hkg1"
{'name': 'Hong Kong, SAR', 'ip': '163.116.200.35'}
```

Example Region Lookup

```commandline
main.py -r "gb"
['eulondon', 'euwest']
```
gtm_data_lookup class

Import Class

```python
from pop_data import gtm_data_lookup

data = gtm_data_lookup.RegionData()
```

Data Files

* region.json - holds all the country to region mappings
* pops.json - regions to primary/secondary pop mappings
* pop_info.json - pop name and ip addresses.
* country_codes.json - mapping of countries to their codes.
** https://raw.githubusercontent.com/unicode-cldr/cldr-localenames-full/master/main/en/territories.json

