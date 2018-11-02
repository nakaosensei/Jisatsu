import ocurrences as ocorrencias

class Decoder:

    def decodeAndWrite(self,stringInput):
        ocurrences = ocorrencias.OcurrencesManager()#Classe dentro de PlantOcurrence.py
        instances=self.getStringsBetween(stringInput,'<td><span onClick="top.getDetail','</td></span>')
        for instance in instances:
            plant = self.getStringsBetweenS(instance,'<span class=\'tG','</span>')
            plant = plant +" " + self.getStringsBetweenS(instance,'<span class=\'tE','</span>')
            plant = plant +" " + self.getStringsBetweenS(instance,'<span class=\'tA','</span>')
            owner = self.getStringsBetweenS(instance,'<span class=\'cL\'>','</span>')
            location = self.getStringsBetweenS(instance,'<span class=\'lP\'>','</span>')
            estado = self.getStringsBetweenS(instance,'<span class=\'lS\'>','</span>')
            cidade = self.getStringsBetweenS(instance,'<span class=\'lM\'>','</span>')
            pais = self.getStringsBetweenS(instance,'<span class=\'lC\'>','</span>')
            latitude = self.getStringsBetweenS(instance,'<i>lat: </i>','</span>')
            longitude = self.getStringsBetweenS(instance,'<i>long: </i>','</span>')
            data = self.getStringsBetweenS(instance,'<span class=\'tY\'>','</span>')
            ocurrences.add("specieslink",plant,owner,location,pais,estado,cidade,latitude,longitude,data)
        ocurrences.cleanAllTrash()
        ocurrences.tratarDatas()
        ocurrences.writeAllToDb()
        print("Ocorrencias escritas no banco...")

    def getStringsBetween(self,stringInput,startStr,endStr):
        vet = stringInput.split(startStr)
        out=[]
        for i in range(1, len(vet)):
            vet2 = vet[i].split(endStr)
            out.append(vet2[0])
        return out

    def getStringsBetweenS(self,stringInput,startStr,endStr):
        vet = stringInput.split(startStr)
        out=""
        for i in range(1, len(vet)):
            vet2 = vet[i].split(endStr)
            out+=vet2[0]
        return out





#decoder = Decoder()
#fileNk = open('generatedDocs/requestText3.json','r')
#decoder.decodeAndWrite(fileNk.read())
