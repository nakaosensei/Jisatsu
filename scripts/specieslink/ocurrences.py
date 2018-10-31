import fileNk
import csv
import planilha
import connection as con

class OcurrencesManager:

    def __init__(self):
        self.ocurrences = []
        self.daoOcurrence = con.DAOOcurrence()

    def add(self,resource,plant,owner,locationDesc,country,state,city,latitude,longitude,dataColeta):
        self.ocurrences.append(PlantOcurrence(plant,owner,locationDesc,country,state,city,latitude,longitude,dataColeta,resource))


    def cleanAllTrash(self):
        for ocurrence in self.ocurrences:
            ocurrence.cleanTrash()

    def printAll(self):
        print(len(self.ocurrences))
        for ocurrence in self.ocurrences:
            ocurrence.print()


    def convertAllToCsv(self):
        planilhaObj = planilha.Planilha()
        ocurrencesStringArrays = []
        for ocurrence in self.ocurrences:
            ocurrencesStringArrays.append(ocurrence.toArray())
        planilhaObj.writeCsv('generatedDocs/speciesLink.csv',['planta','coletador','local','pais','estado','cidade','latitude','longitude','data'],ocurrencesStringArrays)

    def writeAllToDb(self):
        ocurrencesStringArrays = []
        for ocurrence in self.ocurrences:
            ocurrencesStringArrays.append(ocurrence.toDatabaseFormat())
        print(ocurrencesStringArrays)
        self.daoOcurrence.insertOcurrences(ocurrencesStringArrays)

class PlantOcurrence:

    def __init__(self,plant,owner,locationDesc,country,state,city,latitude,longitude,dataColeta,resource):
        self.plant=plant
        self.owner=owner
        self.locationDesc=locationDesc
        self.country=country
        self.state=state
        self.city=city
        self.latitude=latitude
        self.longitude=longitude
        self.dataColeta=dataColeta
        self.anoColeta=""
        self.mesColeta=""
        self.diaColeta=""
        self.resource=resource

    def print(self):
        print("Planta:"+self.plant+"\n"+"Coletado por:"+self.owner+"\nLocalidade:"+self.locationDesc+"\nPais:"+self.country+"\nEstado:"+self.state+"\nCidade:"+self.city+"\nLatitude:"+self.latitude+"\nLongitude:"+self.longitude+"\nDataColeta:"+self.dataColeta+"\n")

    def toCsvFormat(self):
        return self.plant+","+self.owner+","+self.locationDesc+","+self.country+","+self.state+","+self.city+","+self.latitude+","+self.longitude+","+self.dataColeta+"\n"

    def toArray(self):
        return [self.plant,self.owner,self.locationDesc,self.country,self.state,self.city,self.latitude,self.longitude,self.dataColeta]

    def toDatabaseFormat(self):
        return (self.resource,self.plant,self.owner,self.locationDesc,self.country,self.state,self.city,self.latitude,self.longitude,self.anoColeta,self.mesColeta,self.diaColeta)

    def cleanTrash(self):
        self.plant = self.plant.replace("<u>","")
        self.plant = self.plant.replace("</u>","")
        self.plant = self.plant.replace("a'>","")
        self.plant = self.plant.replace("b'>","")
        self.plant = self.plant.replace("c'>","")
        self.plant = self.plant.replace("d'>","")
        self.plant = self.plant.replace("e'>","")
        self.plant = self.plant.replace("f'>","")
        self.plant = self.plant.replace("g'>","")
        self.plant = self.plant.replace("h'>","")
        self.plant = self.plant.replace("i'>","")
        self.plant = self.plant.replace("j'>","")
        self.plant = self.plant.replace("k'>","")
        self.plant = self.plant.replace("l'>","")
        self.plant = self.plant.replace("m'>","")
        self.plant = self.plant.replace("n'>","")
        self.plant = self.plant.replace("o'>","")
        self.plant = self.plant.replace("p'>","")
        self.plant = self.plant.replace("q'>","")
        self.plant = self.plant.replace("r'>","")
        self.plant = self.plant.replace("s'>","")
        self.plant = self.plant.replace("t'>","")
        self.plant = self.plant.replace("u'>","")
        self.plant = self.plant.replace("v'>","")
        self.plant = self.plant.replace("w'>","")
        self.plant = self.plant.replace("x'>","")
        self.plant = self.plant.replace("y'>","")
        self.plant = self.plant.replace("z'>","")
        self.plant = self.plant.replace("'>","")
        empty = "  "
        while(empty in self.plant):
            self.plant = self.plant.replace("  "," ")
        self.plant = self.plant.strip()

        self.plant=self.plant.replace("\t"," ")
        self.owner=self.owner.replace("\t"," ")
        self.locationDesc=self.locationDesc.replace("\t"," ")
        self.country=self.country.replace("\t"," ")
        self.state=self.state.replace("\t"," ")
        self.city=self.city.replace("\t"," ")
        self.latitude=self.latitude.replace("\t"," ")
        self.longitude=self.longitude.replace("\t"," ")
        self.dataColeta=self.dataColeta.replace("\t"," ")

        self.plant=self.plant.replace(";","-")
        self.owner=self.owner.replace(";","-")
        self.locationDesc=self.locationDesc.replace(";","-")
        self.country=self.country.replace(";","-")
        self.state=self.state.replace(";","-")
        self.city=self.city.replace(";","-")
        self.latitude=self.latitude.replace(";","-")
        self.longitude=self.longitude.replace(";","-")
        self.dataColeta=self.dataColeta.replace(";","-")

        
