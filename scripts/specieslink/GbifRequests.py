import requests
from bs4 import BeautifulSoup
import json
import pandas as pd
import sys
import planilha as pl
import connection as con
import ocurrences as oc

class GbifRequests:

    def __init__(self):
        self.daoOcurrence = con.DAOOcurrence()


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

    def makeRequests(self,macrofitasXls):
        plantsOcurrences = {}
        planilha = pl.Planilha()
        p = planilha.openPlantsXls(macrofitasXls)
        tmpId = self.searchID(p[0])
        ocurrencesMap = self.getOccurrencesFromSpecies(tmpId)
        ocurrencesManager = oc.OcurrencesManager()
        for ocurrence in ocurrencesMap:
            species = ocurrence.get("acceptedScientificName")
            if(species is None):
                species = p[0]
            owner = ocurrence.get("recordedBy")
            local = ocurrence.get("locality")
            country = ocurrence.get("countryCode")
            state = ocurrence.get("stateProvince")
            city = ocurrence.get("municipality")
            latitude = ocurrence.get("decimalLatitude")
            longitude = ocurrence.get("decimalLongitude")
            date = ocurrence.get("eventDate")
            ocurrencesManager.add("gbif",species,owner,local,country,state,city,latitude,longitude,date)
        #ocurrencesManager.writeAllToDb()

gbifRequester = GbifRequests()
gbifRequester.makeRequests('../ListaMacrofitas.xlsx')
