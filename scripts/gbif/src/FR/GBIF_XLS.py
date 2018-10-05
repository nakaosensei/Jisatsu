


import requests
from bs4 import BeautifulSoup
import json






class GBIF:

    def __init__(self):
        self.result_occ = None
        self.soup = None
        self.result = None
        self.soup_occ = None

    def search(self, plant):

        params = [('q', plant), ('locale', 'en')]

        self.result = {}
        response = requests.get('https://www.gbif.org/api/omnisearch', headers=None, params=params)
        self.soup = BeautifulSoup(response._content, features="html.parser")

        a = json.loads(self.soup.text)

        if a["speciesMatches"]:
            self.result = a["speciesMatches"]["results"][0]
        return self.result

    def occurrence(self):
        """
            "country": "Brazil",
            "countryCode": "BR",
            "county": "Bonito",
            "decimalLatitude": -8.474149827781018,
            "decimalLongitude": -35.727975889622144,
            "dateIdentified": "1997-06-01T00:00:00.000+0000",
            "locality": "Bonito, Reserva Ecol\u00c3\u00b3gica Municipal da Prefeitura de Bonito  Solo areno argiloso.",
            "identifiedBy": "D. C. Wasshausen",
        :return:
        """
        url = "https://api.gbif.org/v1/occurrence/search"
        offset = 0
        params = [
            ('media_type', 'stillImage'),
            ('offset', offset),
            ('taxon_key', self.result["usageKey"])]

        response = requests.get(url, headers=None, params=params)

        self.soup_occ = BeautifulSoup(response._content, features="html.parser")

        a = json.loads(self.soup_occ.text)
        self.result_occ = a["results"]

        if not a["endOfRecords"]:
            offset += 20
            params = [
                ('media_type', 'stillImage'),
                ('offset', offset),
                ('taxon_key', self.result["usageKey"])]

            response = requests.get(url, headers=None, params=params)

            self.soup_occ = BeautifulSoup(response._content, features="html.parser")

            a = json.loads(self.soup_occ.text)
            self.result_occ = self.result_occ + a["results"]
        return self.result_occ

    def print_occ(self):
        print(json.dumps(self.result_occ, sort_keys=True, indent=2, separators=(',', ': ')))

    def print_occ2(self):
        print(json.dumps(self.result, sort_keys=True, indent=2, separators=(',', ': ')))


