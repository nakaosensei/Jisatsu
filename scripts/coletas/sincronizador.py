import GbifRequests as gbif
import FloraRequests as flora
import PlantListRequests as plantList
import SpeciesLinkRequests as speciesLink
import connectionSqlite as con
import planilha as pl
import copy

posInput=0
posNome=1
posAutor=2
posFonte=3
posEstado=4
posGrupoTaxonomico=5
posFamilia=6
posFormaVida=7
posSubstrato=8
posOrigem=9
posEndemismo=10
posOcorrenciasConfirmadas=11
posOcorrenciasPossiveis=12
posDominiosFitogeograficos=13
posTipoVegetacao=14
posPlantaOriginal=15

pOcFonte=1
pOcNome=2
pOcColetador=3
pOcLocation=4
pOcPais=5
pOcEstado=6
pOcCidade=7
pOcLatitude=8
pOcLongitude=9
pOcAnoColeta=10
pOcMesColeta=11
pOcDiaColeta=12


class Sincronizador:

    def __init__(self):
        self.connection = con.Connection()
        self.daoPlant = con.DAOPlant()
        self.daoOcurrence = con.DAOOcurrence()
        self.planilha = pl.Planilha()
        self.plantasCorretas = []

    def syncDatabase(self,listaPlantas):
        copyList = copy.deepcopy(listaPlantas)
        floraReqs = flora.FloraRequests()
        tplReqs = plantList.PlantListRequests()
        gbifReqs = gbif.GbifRequests()
        speciesReqs = speciesLink.SpeciesLinkRequests()
        self.connection.dropAndCreate()
        floraReqs.makeRequests(listaPlantas)
        for notFound in floraReqs.nonExistent:
            if notFound not in(listaPlantas):
                copyList.append(notFound)
        tplReqs.makeRequests(copyList)
        self.mountComparativeCsv(listaPlantas)
        self.mountPlantsTable(listaPlantas)

        gbifReqs.makeRequests(self.plantasCorretas)
        speciesReqs.makeRequests(self.plantasCorretas)

    def mountSinonimosString(self,listaSinonimos):
        out=""
        for sinonimo in listaSinonimos:
            out+=sinonimo[posNome]+","
        return out

    def mountOcurrencesTable(self,listaPlantas):
        if len(self.plantasCorretas)==0:
            self.mountPlantsTable(listaPlantas)
            if len(self.plantasCorretas)==0:
                return 0
        titleArray = ['planta','fonte','nome','coletor','local','pais','estado','cidade','latitude','longitude','ano','mes','dia']
        registers = []
        for plant in self.plantasCorretas:
            ocurrences = self.daoOcurrence.getAllOcurrencesFromPlant(plant)
            for ocurrence in ocurrences:
                registers.append([plant,ocurrence[pOcFonte],ocurrence[pOcNome],ocurrence[pOcColetador],ocurrence[pOcLocation],ocurrence[pOcPais],ocurrence[pOcEstado],ocurrence[pOcCidade],ocurrence[pOcLatitude],ocurrence[pOcLongitude],ocurrence[pOcAnoColeta],ocurrence[pOcMesColeta],ocurrence[pOcDiaColeta]])
        print("gerando tabela ocurrences.csv")
        self.planilha.writeCsv("ocurrences.csv",titleArray,registers)

    def mountPlantsTable(self,listaPlantas):
        titleArray = ['planta','nome','autor','fonte','estado','grupo taxonomico','familia','forma vida','substrato','origem','endemismo','ocorrenciasConfirmadas','ocorrenciasPossiveis','dominiosFitogeograficos','tipoVegetacao','sinonimos']
        registers = []

        for plant in listaPlantas:
            floraPlants = self.daoPlant.getPlantFromSource(plant,"floradobrasil")
            if len(floraPlants)>0:
                floraPlant = floraPlants[0]
                if floraPlant[posEstado]!="nome aceito" and floraPlant[posEstado]!="nome correto":
                    if floraPlant[posPlantaOriginal]!="":
                        references = self.daoPlant.getPlantFromSource(floraPlant[posPlantaOriginal],"floradobrasil")
                        reference = references[0]
                        sinonimos = self.daoPlant.getAllPlantSinonimimos("floradobrasil",reference[posNome])
                        sinonimos = self.mountSinonimosString(sinonimos)
                        registers.append([plant,reference[posNome],reference[posAutor],reference[posFonte],reference[posEstado],reference[posGrupoTaxonomico],reference[posFamilia],reference[posFormaVida],reference[posSubstrato],reference[posOrigem],reference[posEndemismo],reference[posOcorrenciasConfirmadas],reference[posOcorrenciasPossiveis],reference[posDominiosFitogeograficos],reference[posTipoVegetacao],sinonimos])
                    else:
                        tplPlants = self.daoPlant.getPlantFromSource(plant,"theplantlist")
                        if len(tplPlants)>0:
                            tplPlant = tplPlants[0]
                            if tplPlant[posEstado]=="nome aceito":
                                sinonimos = self.daoPlant.getAllPlantSinonimimos("theplantlist",tplPlant[posNome])
                                sinonimos = self.mountSinonimosString(sinonimos)
                                registers.append([plant,tplPlant[posNome],tplPlant[posAutor],tplPlant[posFonte],tplPlant[posEstado],tplPlant[posGrupoTaxonomico],tplPlant[posFamilia],tplPlant[posFormaVida],tplPlant[posSubstrato],tplPlant[posOrigem],tplPlant[posEndemismo],tplPlant[posOcorrenciasConfirmadas],tplPlant[posOcorrenciasPossiveis],tplPlant[posDominiosFitogeograficos],tplPlant[posTipoVegetacao],sinonimos])
                            elif tplPlant[posEstado]=="sinonimo":
                                references = self.daoPlant.getPlantFromSource(tplPlant[posPlantaOriginal],"theplantlist")
                                reference = references[0]
                                sinonimos = self.daoPlant.getAllPlantSinonimimos("theplantlist",reference[posNome])
                                sinonimos = self.mountSinonimosString(sinonimos)
                                registers.append([plant,reference[posNome],reference[posAutor],reference[posFonte],reference[posEstado],reference[posGrupoTaxonomico],reference[posFamilia],reference[posFormaVida],reference[posSubstrato],reference[posOrigem],reference[posEndemismo],reference[posOcorrenciasConfirmadas],reference[posOcorrenciasPossiveis],reference[posDominiosFitogeograficos],reference[posTipoVegetacao],sinonimos])
                else:
                    sinonimos = self.daoPlant.getAllPlantSinonimimos("floradobrasil",floraPlant[posNome])
                    sinonimos = self.mountSinonimosString(sinonimos)
                    registers.append([plant,floraPlant[posNome],floraPlant[posAutor],floraPlant[posFonte],floraPlant[posEstado],floraPlant[posGrupoTaxonomico],floraPlant[posFamilia],floraPlant[posFormaVida],floraPlant[posSubstrato],floraPlant[posOrigem],floraPlant[posEndemismo],floraPlant[posOcorrenciasConfirmadas],floraPlant[posOcorrenciasPossiveis],floraPlant[posDominiosFitogeograficos],floraPlant[posTipoVegetacao],sinonimos])
            else:
                tplPlants = self.daoPlant.getPlantFromSource(plant,"theplantlist")
                if len(tplPlants)>0:
                    tplPlant = tplPlants[0]
                    if tplPlant[posEstado]=="nome aceito":
                        sinonimos = self.daoPlant.getAllPlantSinonimimos("theplantlist",tplPlant[posNome])
                        sinonimos = self.mountSinonimosString(sinonimos)
                        registers.append([plant,tplPlant[posNome],tplPlant[posAutor],tplPlant[posFonte],tplPlant[posEstado],tplPlant[posGrupoTaxonomico],tplPlant[posFamilia],tplPlant[posFormaVida],tplPlant[posSubstrato],tplPlant[posOrigem],tplPlant[posEndemismo],tplPlant[posOcorrenciasConfirmadas],tplPlant[posOcorrenciasPossiveis],tplPlant[posDominiosFitogeograficos],tplPlant[posTipoVegetacao],sinonimos])
                    elif tplPlant[posEstado]=="sinonimo":
                        references = self.daoPlant.getPlantFromSource(tplPlant[posPlantaOriginal],"theplantlist")
                        reference = references[0]
                        sinonimos = self.daoPlant.getAllPlantSinonimimos("theplantlist",reference[posNome])
                        sinonimos = self.mountSinonimosString(sinonimos)
                        registers.append([plant,reference[posNome],reference[posAutor],reference[posFonte],reference[posEstado],reference[posGrupoTaxonomico],reference[posFamilia],reference[posFormaVida],reference[posSubstrato],reference[posOrigem],reference[posEndemismo],reference[posOcorrenciasConfirmadas],reference[posOcorrenciasPossiveis],reference[posDominiosFitogeograficos],reference[posTipoVegetacao],sinonimos])
        for register in registers:
            self.plantasCorretas.append(register[posNome])
        self.plantasCorretas = self.planilha.reducePlants(self.plantasCorretas)
        self.planilha.writeCsv("plants.csv",titleArray,registers)
        print("Planilha plants.csv gerada")



    def mountComparativeCsv(self,listaPlantas):
        titleArray = ['planta','flora nome','flora status','plant nome','plant status','comparacao']
        registers = []
        for plant in listaPlantas:
            floraPlants = self.daoPlant.getPlantFromSource(plant,"floradobrasil")
            tplPlants = self.daoPlant.getPlantFromSource(plant,"theplantlist")

            if len(floraPlants)>0 and len(tplPlants)>0:
                floraPlant = floraPlants[0]
                tplPlant = tplPlants[0]
                comparison = ""
                state = floraPlant[posEstado]
                if(state=="nome correto"):
                    state="nome aceito"
                if state==tplPlant[posEstado]:
                    comparison="igual"
                else:
                    comparison="diferente"
                registers.append([plant,floraPlant[posNome],state,tplPlant[posNome],tplPlant[posEstado],comparison])
            elif len(floraPlants)>0:
                floraPlant = floraPlants[0]
                state = floraPlant[posEstado]
                if(state=="nome correto"):
                    state="nome aceito"
                registers.append([plant,floraPlant[posNome],state,"none","none","diferente"])
            elif len(tplPlants)>0:
                tplPlant = tplPlants[0]
                registers.append([plant,"none","none",tplPlant[posNome],tplPlant[posEstado],"diferente"])
            else:
                registers.append([plant,"none","none","none","none","igual"])
        self.planilha.writeCsv("flora_vs_plant.csv",titleArray,registers)
        print("Planilha flora_vs_plant.csv gerada")


#s = Sincronizador()
#planilha = pl.Planilha()
#plants = planilha.openPlantsXls("../ListaMacrofitas.xlsx")
#s.syncDatabase(plants)
#s.mountComparativeCsv(plants)
#s.mountPlantsTable(plants)
#s.mountOcurrencesTable(plants)
