import requests
import planilha
import decoder

class requestMaker:

    def makeRequests(self,macrofitasList):
        p = planilha.openPlantsXls('../ListaMacrofitas.xlsx')


    def writeToFile(self):
        file = open("generatedDocs/requestText4.json","w")
        file.write(self.response.text)
        file.close()

requester = requestMaker()


class speciesRequest:
    bigRequestText=""
    hasMore=1

    def __init__(self,species):
        self.species=species
        self.decoderNk = decoder.Decoder()
        bigRequestText=""
        hasMore=1

    def makeRequests(self):
        offset = 0
        while(hasMore==1):
            self.makeRequest(offset)
            offset+=100
        self.decoderNk.decodeAndWriteCsv(bigRequestText)
        hasMore=1
        bigRequestText=""

    def makeRequest(offset):
        self.response = requests.post('http://www.splink.org.br/mod_perl/searchHint', data = {'ts_any':self.species,'offset':offset})
        if('<td><span onClick="top.getDetail' in self.response.text):
            bigRequestText+=self.response.text
        else:
            hasMore=0
