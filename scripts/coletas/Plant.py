import connectionSqlite as con

class PlantsManager:

    def __init__(self):
        self.plants=[]
        self.sinonimos=[]
        self.daoPlants = con.DAOPlant()

    def addPlant(self,nome,autor,fonte,estado,grupoTaxonomico,familia,formaVida,substrato,origem,endemismo,ocorrenciasConfirmadas,ocorrenciasPossiveis,dominiosFitogeograficos,tipoVegetacao,plantaOriginal):
        self.plants.append(Plant(nome,autor,fonte,estado,grupoTaxonomico,familia,formaVida,substrato,origem,endemismo,ocorrenciasConfirmadas,ocorrenciasPossiveis,dominiosFitogeograficos,tipoVegetacao,plantaOriginal))

    def printAll(self):
        for plant in self.plants:
            print(plant.toDatabaseFormat())

    def writeAllToDb(self):
        plantStringArrays = []
        sinonimos = []
        for plant in self.plants:
            plantStringArrays.append(plant.toDatabaseFormat())
        self.daoPlants.insertPlants(plantStringArrays)

class Plant:

    def __init__(self,nome,autor,fonte,estado,grupoTaxonomico,familia,formaVida,substrato,origem,endemismo,ocorrenciasConfirmadas,ocorrenciasPossiveis,dominiosFitogeograficos,tipoVegetacao,plantaOriginal):
        self.nome=nome
        self.autor=autor
        self.fonte=fonte
        self.estado=estado
        self.grupoTaxonomico=grupoTaxonomico
        self.familia=familia
        self.formaVida=formaVida
        self.substrato=substrato
        self.origem=origem
        self.endemismo=endemismo
        self.ocorrenciasConfirmadas=ocorrenciasConfirmadas
        self.ocorrenciasPossiveis=ocorrenciasPossiveis
        self.dominiosFitogeograficos=dominiosFitogeograficos
        self.tipoVegetacao=tipoVegetacao
        self.plantaOriginal=plantaOriginal

    def toDatabaseFormat(self):
        return (self.nome.strip(),self.autor,self.fonte,self.estado,self.grupoTaxonomico,self.familia,self.formaVida,self.substrato,self.origem,self.endemismo,self.ocorrenciasConfirmadas,self.ocorrenciasPossiveis,self.dominiosFitogeograficos,self.tipoVegetacao,self.plantaOriginal)
