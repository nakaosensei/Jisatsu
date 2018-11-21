import connection as con

class PlantManager:

    def __init__(self):
        self.plants=[]
        self.sinonimos=[]
        self.daoPlant = con.DAOPlant()

    def addPlant(self,nome,fonte,estado,hierarquia,familia,formaVida,substrato,possiveisOcorrencias,dominiosFitogeograficos,tipoVegetacao):
        self.plants.append(Plant(nome,fonte,estado,hierarquia,familia,formaVida,substrato,possiveisOcorrencias,dominiosFitogeograficos,tipoVegetacao))

    def addSinonimo(self,nome,fonte,estado,hierarquia,familia,formaVida,substrato,possiveisOcorrencias,dominiosFitogeograficos,tipoVegetacao,nomeOriginal):
        p = Plant(nome,fonte,estado,hierarquia,familia,formaVida,substrato,possiveisOcorrencias,dominiosFitogeograficos,tipoVegetacao)
        p.nomeCorreta=nomeOriginal
        self.sinonimos.append(p)

    def printAll(self):
        for plant in plants:
            plant.print()

    def writeAllToDb(self):
        plantArray = []
        sinoArray = []
        for plant in self.plants:
            plantArray.append(plant.toPlantDatabaseFormat())
        for sinonimo in self.sinonimos:
            sinoArray.append(sinonimo.toSinonimoDatabaseFormat())
        self.daoPlant.insertPlants(plantArrays)
        self.daoPlant.insertSinonimos(plantArrays)
        
class Plant:

    def __init__(self,nome,fonte,estado,hierarquia,familia,formaVida,substrato,possiveisOcorrencias,dominiosFitogeograficos,tipoVegetacao):
        self.nome=nome
        self.fonte=fonte
        self.estado=estado
        self.hierarquia=hierarquia
        self.familia=familia
        self.formaVida=formaVida
        self.substrato=substrato
        self.possiveisOcorrencias=possiveisOcorrencias
        self.dominiosFitogeograficos=dominiosFitogeograficos
        self.tipoVegetacao=tipoVegetacao
        self.nomeCorreta=""

    def toPlantDatabaseFormat(self):
        return (self.nome,self.fonte,self.estado,self.hierarquia,self.familia,self.formaVida,self.substrato,self.possiveisOcorrencias,self.dominiosFitogeograficos,self.tipoVegetacao)

    def toSinonimoDatabaseFormat(self):
        return (self.nome,self.fonte,self.estado,self.hierarquia,self.familia,self.formaVida,self.substrato,self.possiveisOcorrencias,self.dominiosFitogeograficos,self.tipoVegetacao,self.nomeCorreta)


    def print(self):
        print("nome:"+self.nome)
        print("fonte:"+self.fonte)
        print("estado:"+self.estado)
        print("hierarquia:"+self.hierarquia)
        print("familia:"+self.familia)
        print("formaVida:"+self.formaVida)
        print("substrato:"+self.substrato)
        print("possiveisOcorrencias:"+self.possiveisOcorrencias)
        print("dominiosFitogeograficos:"+self.dominiosFitogeograficos)
        print("tipoVegetacao:"+self.tipoVegetacao)
