import requests
import planilha as pl
import decoder as decod

class RequestMaker:

    def __init__(self):
        self.decoder = decod.Decoder()

    def makeRequests(self,macrofitasXls):
        planilha = pl.Planilha()
        p1 = planilha.openPlantsXls(macrofitasXls)
        #p = planilha.listStartsWith(p1,'Dactyloctenium aegyptium')
        for plant in p:
            request = SpeciesRequest(plant,self.decoder)
            request.makeRequests()

        #request = SpeciesRequest(p[0],self.decoder,1)
        #request.makeRequests()

class SpeciesRequest:

    def __init__(self,species,decoder,hasMore=1):
        self.species=species
        self.decoderNk = decoder
        self.bigRequestText=""
        self.hasMore=hasMore

    def makeRequests(self):
        offset = 0
        while(self.hasMore==1):
            self.makeRequest(offset)
            offset+=100
        self.decoderNk.decodeAndWrite(self.bigRequestText)
        print(self.species)
        self.hasMore=1
        self.bigRequestText=""

    def makeRequest(self,offset):
        self.response = requests.post('http://www.splink.org.br/mod_perl/searchHint', data = {'ts_any':self.species,'offset':offset})
        if('<td><span onClick="top.getDetail' in self.response.text):
            self.bigRequestText+=self.response.text
        else:
            self.hasMore=0

requester = RequestMaker()
requester.makeRequests('../ListaMacrofitas.xlsx')
