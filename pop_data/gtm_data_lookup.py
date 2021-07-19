import json
import re


class RegionData(object):
    def __init__(self):
        fh = open("./pop_data/pops.json", "r")
        self.pops = json.loads(fh.read())
        fh.close()
        fh = open("./pop_data/country_codes.json", "r")
        self.codes = json.loads(fh.read())
        fh.close()
        fh = open("./pop_data/pop_info.json", "r")
        self.popinfo = json.loads(fh.read())
        fh.close()
        fh = open("./pop_data/region.json")
        self.regions = json.loads(fh.read())
        fh.close()

    def getpop(self, pop_location=None):
        """

        :param pop_location: Pop code ex. AKL1
        :return: Primary and secondary pops to use.
        """
        return self.pops[pop_location]

    def getcountrycode(self, country_name=None):
        """

        :param country_name: Name of the country you need to code for.
        :return: Countries two digit code.
        """
        for line in self.codes['main']['en']["localeDisplayNames"]['territories']:
            cncode = self.codes['main']['en']["localeDisplayNames"]['territories'][line]
            if re.match(country_name + ".*", cncode.lower(), re.I):
                return line

    def getpopinfo(self, pop_code=None):
        """

        :param pop_code: Pop's code for lookup
        :return: Pop name and IP Address
        """
        return self.popinfo[pop_code.upper()]

    def getregion(self, country=None):
        """

        :param country: Country name ex. China
        :return: What region the country is in. ex..main.py -r "CN" ['aphongkong', 'apnorth']
        """
        values = []
        for region in self.regions['data']:
            for member in self.regions['data'][region]['region-members']:
                m = re.match(country, member, re.I)
                if m:
                    values.append(region)

        return values


if __name__ == "__main__":
    pop = RegionData()
    print(pop.getregions())
