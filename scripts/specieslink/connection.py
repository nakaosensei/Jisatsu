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

class DAOOcurrence:

    def __init__(self):
        self.connection=connection
        self.cursor=connection.mydb.cursor()

    #Ocurrences array ja formatado, no formato [ (val1,val2,val3),(val1,val2,val3),... ]
    def insertOcurrences(self,ocurrencesArray):
        sql = "INSERT INTO OCORRENCIA(FONTE,NOME,COLETADOR,LOCATION,PAIS,ESTADO,CIDADE,LATITUDE,LONGITUDE,ANO_COLETA,MES_COLETA,DIA_COLETA) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        self.cursor.executemany(sql,ocurrencesArray)
        self.connection.mydb.commit()
