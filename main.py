from pop_data import gtm_data_lookup
import argparse
import re

data = gtm_data_lookup.RegionData()


def parseargs(args=None):
    if args.lookup:
        poplookup(cliloc=args.lookup)
    elif args.country:
        print(data.getcountrycode(country_name=args.country))
    elif args.info:
        print(data.getpopinfo(pop_code=args.info))
    elif args.region:
        print(data.getregion(country=args.region))
    else:
        print("Error")


def poplookup(cliloc=None):
    if re.match(".*[US|JP|IN|CA|AU]\/.*", cliloc, re.I):
        regdata = data.getregion(country=cliloc)
        for line in regdata:
            print("Region: {} Pops:{}".format(line, data.getpop(pop_location=line)))
    else:
        ctrycode = data.getcountrycode(country_name=cliloc)
        regdata = data.getregion(country=ctrycode)
        print(regdata)
        for line in regdata:
            print("Region: {} Pops:{}".format(line, data.getpop(pop_location=line)))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-l", "--lookup", help="Looks up primary and secondary POPs")
    parser.add_argument("-c", "--country", help="Lookup country code based on country name.")
    parser.add_argument("-i", "--info", help="Lookup POP name and ip address")
    parser.add_argument("-r", "--region", help="Lookup region data for a country/state")
    parseargs(parser.parse_args())

