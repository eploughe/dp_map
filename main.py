from pop_data import gtm_data_lookup
import argparse

data = gtm_data_lookup.RegionData()


def parseargs(args=None):
    if args.lookup:
        print(data.getpop(location=args.lookup))
    elif args.country:
        print(data.getcountrycode(country=args.country))
    elif args.info:
        print(data.getpopinfo(pop=args.info))
    else:
        print("Error")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-l", "--lookup", help="Looks up primary and secondary POPs")
    parser.add_argument("-c", "--country", help="Lookup country code based on country name.")
    parser.add_argument("-i", "--info", help="Lookup POP name and ip address")
    parseargs(parser.parse_args())

