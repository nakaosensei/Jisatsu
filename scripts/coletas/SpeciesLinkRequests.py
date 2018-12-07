import requests
import planilha as pl
import decoder as decod
import fileNk as fnk
import ocurrences as occ
import time

class SpeciesLinkRequests:

    def __init__(self):
        self.decoder = decod.Decoder()
        self.manager = occ.OcurrencesManager()

    def makeRequestsTests(self,macrofitasXls):
        planilha = pl.Planilha()
        p1 = planilha.openPlantsXls(macrofitasXls)
        #p = planilha.listStartsWith(p1,'Dactyloctenium aegyptium')
        for plant in p1:
            request = SpeciesRequest(plant,self.decoder,self.manager)
            request.makeRequests()
        return self.manager

    def makeRequests(self,plants):
        #p = planilha.listStartsWith(p1,'Dactyloctenium aegyptium')
        for plant in plants:
            request = SpeciesRequest(plant,self.decoder,self.manager)
            request.makeRequests()
        return self.manager

class SpeciesRequest:

    def __init__(self,species,decoder,globalManager,hasMore=1):
        self.species=species
        self.decoderNk = decoder
        self.bigRequestText=""
        self.hasMore=hasMore
        self.globalManager=globalManager
        self.file = fnk.File()

    def makeRequests(self):
        offset = 0
        while(self.hasMore==1):
            self.makeRequest(offset)
            offset+=100
        manager = self.decoderNk.decode(self.bigRequestText)
        print(self.species)
        self.hasMore=1
        self.file.writeToFile("outSpecies.txt",self.bigRequestText)
        self.bigRequestText=""
        return manager

    def makeRequest(self,offset):
        try:
            self.response = requests.post('http://www.splink.org.br/mod_perl/searchHint', data = {'ts_any':self.species,'offset':offset})
            if('<td><span onClick="top.getDetail' in self.response.text):
                self.bigRequestText+=self.response.text
                return 1
            else:
                self.hasMore=0
                return 0
        except:
            time.sleep(10)
            return self.makeRequest(offset)
#requester = SpeciesLinkRequests()
#requester.makeRequestsTests('../ListaMacrofitasTests.xlsx')
