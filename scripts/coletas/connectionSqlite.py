import sqlite3

class Connection:

    def __init__(self):
        self.connection = sqlite3.connect('macrofitas.db')
        self.cursor = self.connection.cursor()
        self.createTables()


    def dropTables(self):
        self.cursor.execute(
        """
            DROP TABLE IF EXISTS PLANT;
        """
        )
        self.cursor.execute(
        """
            DROP TABLE IF EXISTS OCORRENCIA;
        """
        )

    def createTables(self):

        self.cursor.execute(
        """
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
        )
        self.cursor.execute(
        """
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
        )


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
        
class DAOOcurrence:

    def __init__(self):
        self.connection=con.connection
        self.cursor=con.cursor

    #Ocurrences array ja formatado, no formato [ (val1,val2,val3),(val1,val2,val3),... ]
    def insertOcurrences(self,ocurrencesArray):
        sql = "INSERT INTO OCORRENCIA(FONTE,NOME,COLETADOR,LOCATION,PAIS,ESTADO,CIDADE,LATITUDE,LONGITUDE,ANO_COLETA,MES_COLETA,DIA_COLETA) VALUES (?,?,?,?,?,?,?,?,?,?,?,?)"
        self.cursor.executemany(sql,ocurrencesArray)
        self.connection.commit()

con = Connection()
daoP = DAOPlant()
list = daoP.getAllPlantsFromSource("floradobrasil")
print(list)
