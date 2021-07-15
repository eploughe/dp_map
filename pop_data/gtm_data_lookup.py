import json
import re


class RegionData(object):
    def __init__(self):
        fh = open("./pop_data/pops.json", "r")
        self.region = json.loads(fh.read())
        fh.close()
        fh = open("./pop_data/country_codes.json", "r")
        self.codes = json.loads(fh.read())
        fh.close()
        fh = open("./pop_data/pop_info.json", "r")
        self.popinfo = json.loads(fh.read())
        fh.close()

    def getpop(self, location=None):
        return self.region[location]

    def getcountrycode(self, country=None):
        for line in self.codes['main']['en']["localeDisplayNames"]['territories']:
            cncode = self.codes['main']['en']["localeDisplayNames"]['territories'][line]
            if re.match(country + ".*", cncode.lower(), re.I):
                return line

    def getpopinfo(self, pop=None):
        return self.popinfo[pop.upper()]


if __name__ == "__main__":
    pop = RegionData()
    print(pop.getpopinfo())
