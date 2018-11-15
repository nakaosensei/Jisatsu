from lxml import html
import requests
from bs4 import BeautifulSoup
import html2text  

def tpl(name):
    search_url = "http://www.theplantlist.org/tpl1.1/search?q="
    ########################

    #CHAVES DE PESQUISA
    key1 = name.replace(" ", "+")
    ######################
    #  print (key1)
    #STRING DE BUSCA QUE SERA CONCATENADA NO LINK
    search = search_url + key1
    #######################################
    #  print (search)
    #REQUISICAO DE CONTEUDO
    searc = requests.get(search)
    webpage = html.fromstring(searc.content)
    href = webpage.xpath('//a/@href')
    conca = str(href[23]) + "?ref=tpl1"
    print (conca)
    tena = "http://www.theplantlist.org"
    concatena = tena + conca  
    #print (concatena)
    content = requests.get(concatena).content
    ######################################

    #BS4 ORGANIZACAO
    soup = BeautifulSoup(content, "lxml")
    #print (soup)
    #all_tables = soup.find_all('table')
    
    text = soup.get_text()
    text = text.replace("  "," ")

    #text = text[871:]
    #print (text)
    sino = []
    acum = {}
    i = 0
    while (acum != "Date supplied"):
        #print (acum)
        acum = text[i:i+13]
        
        i+=1
    sino = text[i+12:]
    #print (sino)
    final = []
    acuma = {}
    j = 0
    while (acuma != "tplTableInit"):
        acuma = sino[j:j+12]
        j+=1
    final = sino[:j-1]
    print (final)

        

    
tpl("Panicum prionitis Nees")


"""CREATE TABLE PLANTATHEPLANTLIST(
	ID INTEGER NOT NULL auto_increment,
	PLANTA VARCHAR(200),	
	AUTOR VARCHAR(200),
	PRIMARY KEY(ID)
);

CREATE TABLE SINONIMOS_PLANTLIST(
	ID INTEGER NOT NULL auto_increment,PLANTATHEPLANTLIST	
	NOME VARCHAR (100),
	ID_PLANTA_CORRETA INTEGER,	
	AUTOR VARCHAR(200),	
	FOREIGN KEY(ID_PLANTA_CORRETA) REFERENCES PLANTATHEPLANTLIST(ID),
	PRIMARY KEY(ID)
);"""