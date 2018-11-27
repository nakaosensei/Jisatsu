import requests
from bs4 import BeautifulSoup
import json
import pandas as pd
import sys
import planilha as pl
import connection as con
import ocurrences as oc

class GbifRequests:

    def __init__(self,mode):
        self.daoOcurrence = con.DAOOcurrence()

    def searchIDS(self, plant):
        ids = []
        params = [('q', plant), ('locale', 'en')]
        self.speciesID = {}
        response = requests.get('https://www.gbif.org/api/omnisearch', headers=None, params=params)
        self.soup = BeautifulSoup(response._content, features="html.parser")
        a = json.loads(self.soup.text)
        for result in a["speciesMatches"]["results"]:
            ids.append(result)
        return ids

    def getOccurrencesFromSpecies(self,speciesID):
        url = "https://api.gbif.org/v1/occurrence/search"
        offset = 0
        params = [('taxon_key', speciesID["usageKey"])]
        response = requests.get(url, headers=None, params=params)
        data = response.json()
        results = data.get("results")
        return results

    def makeRequests(self,macrofitasXls):
        plantsOcurrences = {}
        planilha = pl.Planilha()
        p = planilha.openPlantsXls(macrofitasXls)
        for plant in p:
            tmpIds = self.searchIDS(plant)
            for tmpId in tmpIds:
                ocurrencesMap = self.getOccurrencesFromSpecies(tmpId)
                ocurrencesManager = oc.OcurrencesManager()
                for ocurrence in ocurrencesMap:
                    species = ocurrence.get("acceptedScientificName")
                    if(species is None):
                        species = plant
                    owner = ocurrence.get("recordedBy")
                    local = ocurrence.get("locality")
                    country = ocurrence.get("countryCode")
                    state = ocurrence.get("stateProvince")
                    city = ocurrence.get("municipality")
                    latitude = ocurrence.get("decimalLatitude")
                    longitude = ocurrence.get("decimalLongitude")
                    date = ocurrence.get("eventDate")
                    ocurrencesManager.add("gbif",species,owner,local,country,state,city,latitude,longitude,date)
                    print(species)
                    print("\n")
                    print(ocurrence)
                    print("\n")
                ocurrencesManager.tratarDatas()
                print(species)
        return ocurrencesManager


gbifRequester = GbifRequests()
manager = gbifRequester.makeRequests('../ListaMacrofitas.xlsx')
manager.writeAllToDb()