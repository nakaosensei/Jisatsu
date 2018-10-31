import pandas as pd
import csv

class Planilha:

    def openPlantsXls(self,filePath):
        df = pd.read_excel(filePath ,header=None)
        plants = df[0]
        return self.reducePlants(plants)

    def writeCsv(self,file,titleArray,valuesArray):
        with open(file, mode='w') as csvFile:
            writer = csv.writer(csvFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            writer.writerow(titleArray)
            for value in valuesArray:
                writer.writerow(value)

    def reducePlants(self,plantList):
        newList = []
        for plant in plantList:
            tmp = ""
            index = plant.find("(")
            if(index!=-1):
                for i in range(0,index-1):
                    tmp+=plant[i]
            else:
                tmp = plant
            if (tmp not in newList):
                newList.append(tmp)
        return newList

#p = Planilha()
#plants = p.openPlantsXls('../ListaMacrofitas.xlsx')
#print(len(plants))
