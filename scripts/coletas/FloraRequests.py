import planilha as pl
import requests
import fileNk as file
import json
import FloraDecoder as decod
import connectionSqlite as conSqlt
import time

class FloraRequests:

    def __init__(self):
        self.decoder = decod.FloraDecoder()
        self.sinonimos = []
        self.nonExistent = []

    def makeRequestsTest(self,macrofitasXls):
        planilha = pl.Planilha()
        p = planilha.openPlantsXls(macrofitasXls)
        #p = planilha.listStartsWith(p,'Stemodia pratensis')
        for plant in p:
            print(plant)
            frequest = FloraRequest(plant)
            result = frequest.makeRequest()
            if result!=1 and result!=0:
                self.sinonimos.append(plant)
                request2 = FloraRequest(result)
                request2.makeRequest()
            elif result==0:
                self.nonExistent.append(plant)
        print("Nonexistents on Flora")
        for nonExistent in self.nonExistent:
            print(nonExistent)

    def makeRequests(self,plants):
        for plant in plants:
            print(plant)
            frequest = FloraRequest(plant)
            result = frequest.makeRequest()
            if result!=1 and result!=0:
                self.sinonimos.append(plant)
                request2 = FloraRequest(result)
                request2.makeRequest()
            elif result==0:
                self.nonExistent.append(plant)
        print("Nonexistents on Flora")
        for nonExistent in self.nonExistent:
            print(nonExistent)




class FloraRequest:

    def __init__(self,species):
        self.species = species
        self.parsedSpeciesAPI = self.parseSpecieAPI()
        self.parsedSpecies = self.parseSpecie()
        self.fileManager = file.File()
        self.idDadosListaBrasil=""
        self.requestPiloto=""
        self.request=""

    def parseSpecieAPI(self):
        splitStr = self.species.split(" ")
        outStr = ""
        for i in range(0,len(splitStr)):
            if i==(len(splitStr)-1):
                outStr+=splitStr[i]
            else:
                outStr+=splitStr[i]+"_"
        return outStr

    def parseSpecie(self):
        splitStr = self.species.split(" ")
        outStr = ""
        for i in range(0,len(splitStr)):
            if i==(len(splitStr)-1):
                outStr+=splitStr[i]
            else:
                outStr+=splitStr[i]+"+"
        return outStr

    def processRequest(self):
        link = "http://floradobrasil.jbrj.gov.br/reflora/listaBrasil/ConsultaPublicaUC/BemVindoConsultaPublicaConsultar.do?invalidatePageControlCounter=20&idsFilhosAlgas=[2]&idsFilhosFungos=[1%2C10%2C11]&lingua=pt&grupo=5&familia=null&genero=&especie=&autor=&nomeVernaculo=&nomeCompleto="+self.parsedSpecies+"&formaVida=null&substrato=null&ocorreBrasil=QUALQUER&ocorrencia=OCORRE&endemismo=TODOS&origem=TODOS&regiao=QUALQUER&estado=QUALQUER&ilhaOceanica=32767&domFitogeograficos=QUALQUER&bacia=QUALQUER&vegetacao=TODOS&mostrarAte=SUBESP_VAR&opcoesBusca=TODOS_OS_NOMES&loginUsuario=Visitante&senhaUsuario=&contexto=consulta-publica"

        self.requestPiloto = requests.get(link)
        self.idDadosListaBrasil = self.getStringsBetweenS(self.requestPiloto.text,"<input type=\"hidden\" name=\"idDadosListaBrasil\"","id=\"carregaTaxonGrupoIdDadosListaBrasil\">")
        self.idDadosListaBrasil = self.getStringsBetweenS(self.idDadosListaBrasil,"value=\"","\"")
        newLink = "http://floradobrasil.jbrj.gov.br/reflora/listaBrasil/ConsultaPublicaUC/ResultadoDaConsultaCarregaTaxonGrupo.do?&idDadosListaBrasil="+self.idDadosListaBrasil
        self.request = requests.get(newLink)
        if self.request.text.strip()=="erro":
            return 0
        decoder = decod.FloraDecoder()
        result = decoder.decodeRequestAndWriteToDb(self.request.json())
        return result

    def makeRequest(self):
        try:
            return self.processRequest()
        except:
            time.sleep(10)
            return self.processRequest()

    def makeRequestApi(self):
        self.request=requests.get("http://servicos.jbrj.gov.br/flora/taxon/"+self.parsedSpeciesAPI)
        json = self.request.json()
        print(json["result"])

    def getStringsBetweenS(self,stringInput,startStr,endStr):
        vet = stringInput.split(startStr)
        out=""
        for i in range(1, len(vet)):
            vet2 = vet[i].split(endStr)
            out+=vet2[0]
        return out

#con = conSqlt.Connection()
#con.dropAndCreate()

#freqs = FloraRequests()
#freqs.makeRequestsTest("../ListaMacrofitas.xlsx")

#testSinonimo = "Limnobium bogotense"
#testCorreto = "Limnobium laevigatum"
#testAlternativo = "Hygrophila guianensis"
#request = FloraRequest(testAlternativo)
#result = request.makeRequest()
#print(result)
#if result!=1:
#    req2 = FloraRequest(result)
#    req2.makeRequest()
