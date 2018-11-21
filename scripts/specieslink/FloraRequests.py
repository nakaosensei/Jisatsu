import planilha as pl
import requests
import fileNk as file
import json
import FloraDecoder as decod

class FloraRequests:

    def __init__():
        self.decoder = decod.FloraDecoder()
        self.sinonimos = []

    def makeRequests(self,macrofitasXls):
        planilha = pl.Planilha()
        p = planilha.openPlantsXls(macrofitasXls)
        #p = planilha.listStartsWith(p1,'Dactyloctenium aegyptium')
        for plant in p:
            frequest = FloraRequest(plant)
            result = frequest.makeRequest()
            if result!=1:
                self.sinonimos.append(plant)
                request2 = FloraRequest(result)
                request2.makeRequest()
        for sinonimo in self.sinonimos:
            print(sinonimo)


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

    def makeRequest(self):
         link = "http://floradobrasil.jbrj.gov.br/reflora/listaBrasil/ConsultaPublicaUC/BemVindoConsultaPublicaConsultar.do?invalidatePageControlCounter=20&idsFilhosAlgas=[2]&idsFilhosFungos=[1%2C10%2C11]&lingua=pt&grupo=5&familia=null&genero=&especie=&autor=&nomeVernaculo=&nomeCompleto="+self.parsedSpecies+"&formaVida=null&substrato=null&ocorreBrasil=QUALQUER&ocorrencia=OCORRE&endemismo=TODOS&origem=TODOS&regiao=QUALQUER&estado=QUALQUER&ilhaOceanica=32767&domFitogeograficos=QUALQUER&bacia=QUALQUER&vegetacao=TODOS&mostrarAte=SUBESP_VAR&opcoesBusca=TODOS_OS_NOMES&loginUsuario=Visitante&senhaUsuario=&contexto=consulta-publica"
         self.requestPiloto = requests.get(link)
         self.idDadosListaBrasil = self.getStringsBetweenS(self.requestPiloto.text,"<input type=\"hidden\" name=\"idDadosListaBrasil\"","id=\"carregaTaxonGrupoIdDadosListaBrasil\">")
         self.idDadosListaBrasil = self.getStringsBetweenS(self.idDadosListaBrasil,"value=\"","\"")
         newLink = "http://floradobrasil.jbrj.gov.br/reflora/listaBrasil/ConsultaPublicaUC/ResultadoDaConsultaCarregaTaxonGrupo.do?&idDadosListaBrasil="+self.idDadosListaBrasil
         self.request = requests.get(newLink)
         self.fileManager.writeToFile("outFloraCru.txt",self.requestPiloto.text)
         self.fileManager.writeToFile("outFloraListaBrasil.txt",self.request.text)
         decoder = decod.FloraDecoder()
         return decoder.decodeRequestAndWriteToDb(self.request.json())


    def makeRequestApi(self):
        self.request=requests.get("http://servicos.jbrj.gov.br/flora/taxon/"+self.parsedSpeciesAPI)
        self.fileManager.writeToFile("outFlora.txt",self.request.text)
        json = self.request.json()
        print(json["result"])

    def getStringsBetweenS(self,stringInput,startStr,endStr):
        vet = stringInput.split(startStr)
        out=""
        for i in range(1, len(vet)):
            vet2 = vet[i].split(endStr)
            out+=vet2[0]
        return out

#freqs = FloraRequests()
#freqs.makeRequests("../ListaMacrofitas.xlsx")
testSinonimo = "Limnobium bogotense"
testCorreto = "Limnobium laevigatum"
request = FloraRequest(testSinonimo)
result = request.makeRequest()
print(result)
if result!=1:
    req2 = FloraRequest(result)
    req2.makeRequest()
