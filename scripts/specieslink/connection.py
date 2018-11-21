import mysql.connector

class Connection:

    def __init__(self):
        self.mydb = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        passwd="root",
        database="Macrofitas"
    )

connection = Connection()

class DAOPlant:

    def __init__(self):
        self.connection=connection
        self.cursor=connection.mydb.cursor()

    def insertPlants(self,plantsArray):
        sql = "INSERT INTO PLANT(NOME,AUTOR,FONTE,ESTADO,GRUPO_TAXONOMICO,FAMILIA,FORMA_VIDA,SUBSTRATO,ORIGEM,ENDEMISMO,OCORRENCIAS_CONFIRMADAS,OCORRENCIAS_POSSIVEIS,DOMINIOS_FITOGEOGRAFICOS,TIPO_VEGETACAO) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        self.cursor.executemany(sql,plantsArray)
        self.connection.mydb.commit()

    def insertSinonimos(self,sinonimos):
        sql = "INSERT INTO SINONIMO(NOME,AUTOR,FONTE,NOME_CORRETA) VALUES (%s,%s,%s,%s)"
        self.cursor.executemany(sql,sinonimos)
        self.connection.mydb.commit()

class DAOOcurrence:

    def __init__(self):
        self.connection=connection
        self.cursor=connection.mydb.cursor()

    #Ocurrences array ja formatado, no formato [ (val1,val2,val3),(val1,val2,val3),... ]
    def insertOcurrences(self,ocurrencesArray):
        sql = "INSERT INTO OCORRENCIA(FONTE,NOME,COLETADOR,LOCATION,PAIS,ESTADO,CIDADE,LATITUDE,LONGITUDE,ANO_COLETA,MES_COLETA,DIA_COLETA) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        self.cursor.executemany(sql,ocurrencesArray)
        self.connection.mydb.commit()
