import requests
from bs4 import BeautifulSoup
import json
import pandas as pd
import sys
#from Tkinter import Tk
#rom tkinter.filedialog import askopenfilename

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


gbif = GbifRequests()

print(sys.argv[1])
df = pd.read_excel(sys.argv[1] ,header=None)
plants = df[0]
gbifrequests = GbifRequests()
plantsOcurrences = {}


for i in range(len(plants)):
    tmpId = gbifrequests.searchID(plants[i])
    ocurrences = gbifrequests.getOccurrencesFromSpecies(tmpId)
    plantsOcurrences[plants[i]]=ocurrences
