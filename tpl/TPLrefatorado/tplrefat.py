from lxml import html
import requests
from bs4 import BeautifulSoup
import html2text 
###########################################################################
####### BUSCA PELOS SINONIMOS #############################################
###########################################################################
def construUrl(name):
    search_url = "http://www.theplantlist.org/tpl1.1/search?q="
    ########################

    #CHAVES DE PESQUISA
    key1 = name.replace(" ", "+")
    ######################

    #STRING DE BUSCA QUE SERA CONCATENADA NO LINK
    search = search_url + key1
    #######################################
    return search

def requisicaoTPL1(search):
    searc = requests.get(search)
    #print(searc)
    return searc

def procuraHref(searc):
    webpage = html.fromstring(searc.content)

    href = webpage.xpath('//a/@href')
    #print(href)
    return href

def requestHref(href):
    hrefestr = str(href)
    #for i in range(len(href)):
    try : 
        hrefefind = hrefestr.find('/tpl1.1/record/kew-')
        agarrefe = hrefestr[hrefefind:hrefefind+25]
        conca = str(agarrefe) + "?ref=tpl1"
        print(conca)
        tena = "http://www.theplantlist.org"
        concatena = tena + conca  
        retorna = requests.get(concatena).content
    except:
        hrefefind = hrefestr.find('/tpl/record/kew')
        agarrefe = hrefestr[hrefefind:hrefefind+31]
        conca = str(agarrefe) 
        print(conca)
        tena = "http://www.theplantlist.org"
        concatena = tena + conca  
        retorna = requests.get(concatena).content


    #print(hrefestr[hrefefind:hrefefind+25])
    
    return retorna

def requestHrefsec(href):
    hrefestr = str(href)
    hrefefind = hrefestr.find('/tpl/record/kew')
    agarrefe = hrefestr[hrefefind:hrefefind+31]
    conca = str(agarrefe) 
    print(conca)
    tena = "http://www.theplantlist.org"
    concatena = tena + conca  
    print(concatena)
    retorna = requests.get(concatena).content

    #print(hrefestr[hrefefind:hrefefind+25])
    
    return retorna

def trataHref(retorna):
    print("retorna")
    print(retorna)
    soup = BeautifulSoup(retorna, "lxml")
    text = soup.get_text()
    text = text.replace("  "," ")
    #print(text)
    return text
    
def encontraSinonimos2(text):
    text= str(text)
    init = text.find('Source')
    print(init)
    finit = text.find('tplTableInit()')
    print(finit)
    #print("######################",text[init:finit])
    trat = str(text[init+45:finit])
    trat = trat.replace("  ","")
    #trat = trat.replace("\n","")
    print(trat)
    indixe = trat.find('Source')
    trat = trat[indixe+6:]
    listrat = trat.split("\n")
    listrat = set(listrat)

    return listrat

def encontraSinonimos(text):
    #print(text)
    sino = []
    acum = {}
    i = 0

    while (acum != "Date supplied"):
        acum = text[i:i+13]
        i+=1
        if (i > len(text)):
            break
    sino = text[i+12:]
    final = []
    acuma = {}
    j = 0
    while (acuma != "tplTableInit"):
        
        acuma = sino[j:j+12]
        j+=1
        if (j > len(sino)):
            break
    final =sino[:j-1]
    
    resultante = []
    i = 0
    while i < len(final)-1:

        if (final[i] == '\n'):

            barraenes = ''
            i+=1
            while (final[i] != '\n'):

                barraenes= barraenes + final[i]
                i+=1

        if (barraenes != ''):
            resultante.append(barraenes)


    return resultante

#############################################################################
###### BUSCA PELO NOME DO AUTOR #############################################
#############################################################################
#
# Busca ID Ipni #############################################################
def buscaIDIpini(text):
    #print (text)
    inde = text.find('http://ipni')
    indefin = text.find('Synonyms:')

    lipnit = text[inde-1 : indefin-1]
    #print (lipnit)

    if len(lipnit) == 0:
        inde = text.find('urn:lsid:ipni.org')
        indefin = text.find('Synonyms:')
        lipnit = "http://www.ipni.org/ipni/idPlantNameSearch.do?id=" + text[inde+24 : indefin-2]
    last = lipnit[len(lipnit)-1]
    if last == '.':
        lipnit = lipnit[:(len(lipnit)-1)]

    
    #print(lipnit)
    return (lipnit)
    

#
#
# Faz a requisicao do site Ipni #############################################
def reqIpini(linkipnifinal):
    print(linkipnifinal)
    searcipini = requests.get(linkipnifinal).content
    soupin = BeautifulSoup(searcipini, "lxml")
    sotexta = str(soupin)
    if sotexta.find("The International Plant Names Index: Error") != (-1):
        print("Erro")
        
    
    return sotexta
#
#
# Busca a id do autor no texto ##############################################
def idIpiniAutor(sotext):
    #print (sotext)
    indIdAutor = sotext.find('lsid:ipni.org:authors:')

   
    
    indc = sotext.find(" tm:index=")
    idautor = str(sotext[indIdAutor+22:indc-1])
    print (indc)
    if indIdAutor == (-1):
        print ("FALHA AO ENCONTRAR NOME DO AUTOR")
        secind = sotext.find('?id=')
        second = sotext.find('&amp;back_page')
        print(sotext[secind+4:second])
        idautor = str(sotext[secind+4:second])
        
    
    print("ID do autor", idautor)
    

    return idautor
#
#
# Constroi o link Ipni ###################################################### 
def constLinkAutor(idautor):
    print("ID do autor", idautor)
    reqautor = "http://www.ipni.org/ipni/idAuthorSearch.do?id=" + idautor + "&back_page="
    print("Link da requisicao",reqautor)
    return reqautor
#
#
# Faz a requisicao da pagina Ipni do Autor ##################################
def reqAutor(reqautor):
    #print(reqautor)
    reqs = requests.get(reqautor).content
    #print(reqs)
    return reqs

#
#
# Separa os nomes no texto da requisicao #####################################
def trataNomes(reqs):

    soupauto = BeautifulSoup(reqs, "lxml")
    textautor = soupauto.get_text()
    tokun = {}
    xy = 0
  
    if textautor.find("Author Details") == -1:
        return 0

    while tokun != "Author Details":
        tokun=textautor[xy:xy+14]
        xy += 1
    tokun = {}
    while tokun != "Author Details":
        tokun=textautor[xy:xy+14]
        xy += 1
    #print(textautor[xy+13:])
    newtextautor = textautor[xy+13:]
    tokun = {}
    xy = 0
    #print(textautor)
    try: 
        textautor.find("Standard Form:")
    except:
        return False

    while tokun != "Standard Form:":
        tokun = newtextautor[xy:xy+14]
        xy+=1
    textnames = newtextautor[:xy-1]

    ########### 
    textnames = textnames.replace("\n", "")
    textnames = textnames.replace("\t", "")
    #textnames = textnames.replace("(", " (")
    textnames = textnames.replace("  ","")
    listadenome = textnames.split(",")
    listadenomes = list(listadenome)
    return listadenomes
###############################################################################

###############################################################################
def roda(nome):
    print("BUSCANDO PELOS SINONIMOS")
    search = construUrl(nome)
    print(" PT1/6 - OK!")
    searc = requisicaoTPL1(search)
    #print(searc)
    print(" PT2/6 - OK!")
    href = procuraHref(searc)
    #print(href)
    print(" PT3/6 - OK!")
    retorna = requestHref(href)

    print(" PT4/6 - OK!")
    text = trataHref(retorna)
    print(" PT5/6 - OK!")
    resultante = encontraSinonimos(text)
    print (len(resultante))
    if len(resultante) == 0: 
        print(" Refaz PT3/6 - OK!")
        retornao = requestHrefsec(href)
        #print (retorna)
        print(" Refaz PT4/6 - OK!")
        text = trataHref(retornao)
        print(" Refaz PT5/6 - OK!")
        resultante = encontraSinonimos2(text)




    print(" PT6/6 - OK!")

    print("PT1 == OK\n")


    print("BUSCANDO PELOS AUTORES")
    linkipnifinal = buscaIDIpini(text)
    print("PT1/6 - OK!")
    sotext = reqIpini(linkipnifinal)
    print("PT2/6 - OK!")
    #print (sotext)
    idautor = idIpiniAutor(sotext)
    
    print("PT3/6 - OK!")
    #print(idautor)
    reqautor = constLinkAutor(idautor)

    print("PT4/6 - OK!")
    #print(reqautor)
    reqs = reqAutor(reqautor)
    print("PT5/6 - OK!")
    #print(reqs)
    listadenomes = trataNomes(reqs)
    print("PT6/6 - OK!")
    print("#############################################################")
    print (listadenomes)
    print(resultante)
roda("Hygrophila costa")
#roda("Panicum prionitis Nees")
#roda("Echinodorus longipetalus Micheli")