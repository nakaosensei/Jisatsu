import connection as con

class PlantsManager:

    def __init__(self):
        self.plants=[]
        self.sinonimos=[]
        self.daoPlants = con.DAOPlant()

    def addPlant(self,nome,autor,fonte,estado,grupoTaxonomico,familia,formaVida,substrato,origem,endemismo,ocorrenciasConfirmadas,ocorrenciasPossiveis,dominiosFitogeograficos,tipoVegetacao,sinonimos):
        self.plants.append(Plant(nome,autor,fonte,estado,grupoTaxonomico,familia,formaVida,substrato,origem,endemismo,ocorrenciasConfirmadas,ocorrenciasPossiveis,dominiosFitogeograficos,tipoVegetacao,sinonimos))

    def writeAllToDb(self):
        plantStringArrays = []
        sinonimos = []
        for plant in self.plants:
            plantStringArrays.append(plant.toDatabaseFormat())
            if plant.sinonimos is not None:
                sinonimos.append(plant.sinonimos)
        self.daoPlants.insertPlants(plantStringArrays)
        for sinonimosList in sinonimos:
            self.daoPlants.insertSinonimos(sinonimosList)

class Plant:

    def __init__(self,nome,autor,fonte,estado,grupoTaxonomico,familia,formaVida,substrato,origem,endemismo,ocorrenciasConfirmadas,ocorrenciasPossiveis,dominiosFitogeograficos,tipoVegetacao,sinonimos):
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
        self.sinonimos = sinonimos

    def toDatabaseFormat(self):
        return (self.nome,self.autor,self.fonte,self.estado,self.grupoTaxonomico,self.familia,self.formaVida,self.substrato,self.origem,self.endemismo,self.ocorrenciasConfirmadas,self.ocorrenciasPossiveis,self.dominiosFitogeograficos,self.tipoVegetacao)
