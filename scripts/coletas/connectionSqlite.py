import sqlite3

class Connection:

    def __init__(self):
        self.connection = sqlite3.connect('macrofitas.db')
        self.cursor = self.connection.cursor()
        self.dropPlantScript="""
            DROP TABLE IF EXISTS PLANT;
        """
        self.dropOcurrenceScript="""
            DROP TABLE IF EXISTS OCORRENCIA;
        """

        self.createOcurrenceScript="""
        CREATE TABLE IF NOT EXISTS OCORRENCIA(
            ID INTEGER PRIMARY KEY,
            FONTE VARCHAR(100),
        	NOME VARCHAR(200),
        	COLETADOR VARCHAR(200),
        	LOCATION VARCHAR(2000),
        	PAIS VARCHAR(100),
        	ESTADO VARCHAR(100),
        	CIDADE VARCHAR(100),
        	LATITUDE VARCHAR(50),
        	LONGITUDE VARCHAR(50),
        	ANO_COLETA VARCHAR(4),
        	MES_COLETA VARCHAR(2),
        	DIA_COLETA VARCHAR(2)
        );
        """
        self.createPlantScript ="""
            CREATE TABLE IF NOT EXISTS  PLANT(
            ID INTEGER PRIMARY KEY,
        	NOME VARCHAR(200),
            AUTOR VARCHAR(200),
            FONTE VARCHAR(50),
        	ESTADO VARCHAR(10),
        	GRUPO_TAXONOMICO VARCHAR(100),
        	FAMILIA VARCHAR(100),
        	FORMA_VIDA VARCHAR(200),
        	SUBSTRATO VARCHAR(100),
        	ORIGEM VARCHAR(100),
        	ENDEMISMO VARCHAR(100),
            OCORRENCIAS_CONFIRMADAS VARCHAR(500),
        	OCORRENCIAS_POSSIVEIS VARCHAR(500),
        	DOMINIOS_FITOGEOGRAFICOS VARCHAR(500),
        	TIPO_VEGETACAO VARCHAR(500),
        	PLANTA_ORIGINAL VARCHAR(200)
        );
        """
        self.createTables()

    def dropTables(self):
        self.cursor.execute(self.dropPlantScript)
        self.cursor.execute(self.dropOcurrenceScript)

    def createTables(self):
        #self.dropTables()
        self.cursor.execute(self.createOcurrenceScript)
        self.cursor.execute(self.createPlantScript)

    def dropAndCreate(self):
        print("DELETANDO REGISTROS DO BANCO...")
        print("RECRIANDO AS TABELAS...")
        self.dropTables()
        self.createTables()

class DAOPlant:

    def __init__(self):
        self.connection=con.connection
        self.cursor=con.cursor

    def insertPlants(self,plantsArray):
        sql = "INSERT INTO PLANT(NOME,AUTOR,FONTE,ESTADO,GRUPO_TAXONOMICO,FAMILIA,FORMA_VIDA,SUBSTRATO,ORIGEM,ENDEMISMO,OCORRENCIAS_CONFIRMADAS,OCORRENCIAS_POSSIVEIS,DOMINIOS_FITOGEOGRAFICOS,TIPO_VEGETACAO,PLANTA_ORIGINAL) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
        self.cursor.executemany(sql,plantsArray)
        self.connection.commit()

    def getAllPlantsFromSource(self,source):
        self.cursor.execute("SELECT * FROM PLANT WHERE fonte like ?", (source,))
        rows = self.cursor.fetchall()
        return rows

    def getPlantFromSource(self,plant,source):
        self.cursor.execute("SELECT * FROM PLANT WHERE (fonte LIKE ?) AND (nome like ('%' || ? || '%'))", (source,plant,))
        rows = self.cursor.fetchall()
        return rows

    def getAllPlantSinonimimos(self,source,plant):
        self.cursor.execute("SELECT * FROM PLANT WHERE fonte like ? AND PLANTA_ORIGINAL like ? AND ESTADO='sinonimo'", (source,plant,))
        rows = self.cursor.fetchall()
        return rows

    def dropAndCreate(self):
        self.cursor.execute(self.connection.dropPlantScript)
        self.cursor.execute(self.connection.createPlantScript)
        return

    def deleteFromSource(self,source):
        self.cursor.execute("DELETE FROM PLANT WHERE fonte like ?", (source,))
        self.cursor.fetchall()

    def tableIsEmpty(self):
        self.cursor.execute("SELECT COUNT(*) from PLANT")
        count=self.cursor.fetchone()
        print(count)
        if count[0]==0:
            return True
        else:
            return False

class DAOOcurrence:

    def __init__(self):
        self.connection=con.connection
        self.cursor=con.cursor

    #Ocurrences array ja formatado, no formato [ (val1,val2,val3),(val1,val2,val3),... ]
    def insertOcurrences(self,ocurrencesArray):
        sql = "INSERT INTO OCORRENCIA(FONTE,NOME,COLETADOR,LOCATION,PAIS,ESTADO,CIDADE,LATITUDE,LONGITUDE,ANO_COLETA,MES_COLETA,DIA_COLETA) VALUES (?,?,?,?,?,?,?,?,?,?,?,?)"
        self.cursor.executemany(sql,ocurrencesArray)
        self.connection.commit()

    def dropAndCreate(self):
        self.cursor.execute(self.connection.dropOcurrenceScript)
        self.cursor.execute(self.connection.createOcurrenceScript)
        return

    def tableIsEmpty(self):
        self.cursor.execute("SELECT COUNT(*) from OCORRENCIA")
        count=self.cursor.fetchone()
        print(count)
        if count[0]==0:
            return True
        else:
            return False


    def getAllOcurrencesFromSource(self,source):
        self.cursor.execute("SELECT * FROM OCORRENCIA WHERE fonte like ?", (source,))
        rows = self.cursor.fetchall()
        return rows

    def getAllOcurrencesFromPlant(self,plant):
        self.cursor.execute("SELECT * FROM OCORRENCIA WHERE nome like ('%' || ? || '%')", (plant,))
        rows = self.cursor.fetchall()
        return rows

class Tests:
    def testFloraDoBrasil(self):
        print("teste floradobrasil")
        daoP = DAOPlant()
        list = daoP.getAllPlantsFromSource("floradobrasil")
        for elemento in list:
            if elemento[4]!="sinonimo":
                line = "\n"+elemento[1]+",sinonimos:"
                sinonimos = daoP.getAllPlantSinonimimos("floradobrasil",elemento[1])
                for sinonimo in sinonimos:
                    line+=sinonimo[1]+","
                print(line)
        print(len(list))

    def testThePlantList(self):
        print("Teste theplantlist")
        daoP = DAOPlant()
        list = daoP.getAllPlantsFromSource("theplantlist")
        print(list)
        for elemento in list:
            if elemento[4]!="sinonimo":
                line = "\n"+elemento[1]+",sinonimos:"
                sinonimos = daoP.getAllPlantSinonimimos("theplantlist",elemento[1])
                for sinonimo in sinonimos:
                    line+=sinonimo[1]+","
                print(line)
        print(len(list))


    def testGbif(self):
        daoOc = DAOOcurrence()
        ocurrences = daoOc.getAllOcurrencesFromSource("gbif")
        print("Qtde ocorrencias GBIF")
        print(len(ocurrences))
        #for ocurrence in ocurrences:
        #    print(ocurrence)

    def testSpeciesLink(self):
        daoOc = DAOOcurrence()
        ocurrences = daoOc.getAllOcurrencesFromSource("specieslink")
        print("Qtde ocorrencias SpeciesLink")
        print(len(ocurrences))

con = Connection()
#daoP = DAOPlant()
#print(daoP.tableIsEmpty())
#con.dropAndCreate()
#tests = Tests()
#tests.testGbif()
#tests.testSpeciesLink()
#tests.testThePlantList()
#tests.testFloraDoBrasil()
