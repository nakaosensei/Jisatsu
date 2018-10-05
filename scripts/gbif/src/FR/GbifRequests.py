import requests
from bs4 import BeautifulSoup
import json
import pandas as pd

class GbifRequests:

    def searchID(self, plant):
        print(plant)
        params = [('q', plant), ('locale', 'en')]
        self.speciesID = {}
        response = requests.get('https://www.gbif.org/api/omnisearch', headers=None, params=params)
        self.soup = BeautifulSoup(response._content, features="html.parser")
        a = json.loads(self.soup.text)
        if a["speciesMatches"]:
            speciesID = a["speciesMatches"]["results"][0]
        return speciesID

    def getOccurrencesFromSpecies(self,speciesID):
        url = "https://api.gbif.org/v1/occurrence/search"
        offset = 0
        params = [('taxon_key', speciesID["usageKey"])]
        response = requests.get(url, headers=None, params=params)
        data = response.json()
        results = data.get("results")
        return results


if __name__ == "__main__":
    gbif = GbifRequests()
    df = pd.read_excel('ListaMacrofitas.xlsx' ,header=None)
    plants = df[0]
    gbifrequests = GbifRequests()
    plantsOcurrences = {}

    id = gbif.searchID("Hygrophila costata Nees")
    ocurrences = gbif.getOccurrencesFromSpecies(id)
    plantsOcurrences["Hygrophila costata Nees"]=ocurrences
    exemplos = plantsOcurrences["Hygrophila costata Nees"]
    for i in exemplos:
        print(i.keys())
        print("\n")
        print(i.items())
        print("\n")
        
    for i in range(len(plants)):
        tmpId = gbifrequests.searchID(plants[i])
        ocurrences = gbifrequests.getOccurrencesFromSpecies(tmpId)
        plantsOcurrences[plants[i]]=ocurrences
    hyprogripla = plantsOcurrences["Hygrophila costata Nees"]
