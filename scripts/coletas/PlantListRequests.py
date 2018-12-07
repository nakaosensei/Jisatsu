import planilha as pl
import connectionSqlite as conSqlt
import tpl3 as tpl
import time
class PlantListRequests:

    def __init__(self):
        self.decoder = None
        self.nonExistent = []
        self.sinonimos = []

    def makeRequestsTests(self,macrofitasXls):
        planilha = pl.Planilha()
        p = planilha.openPlantsXls(macrofitasXls)
        for plant in p:
            print(plant)
            try:
                result = tpl.roda(plant)
            except:
                time.sleep(10)
                result = tpl.roda(plant)
            if(result)==0:
                self.nonExistent.append(plant)

    def makeRequests(self,plants):
        for plant in plants:
            print(plant)
            try:
                result = tpl.roda(plant)
            except:
                time.sleep(10)
                result = tpl.roda(plant)
            if(result)==0:
                self.nonExistent.append(plant)

#req = PlantListRequests()
#req.makeRequestsTests("../ListaMacrofitas.xlsx")
