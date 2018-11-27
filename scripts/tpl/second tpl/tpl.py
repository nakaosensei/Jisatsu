from lxml import html
import requests
from bs4 import BeautifulSoup
import html2text  
#######################################################################################
##################   RETORNA A LISTA DE SINÔNIMOS #####################################

def tpl(name):
    print(name)
    print("Aguarde o Carregamento = __________")
    search_url = "http://www.theplantlist.org/tpl1.1/search?q="
    ########################

    #CHAVES DE PESQUISA
    key1 = name.replace(" ", "+")
    ######################

    #STRING DE BUSCA QUE SERA CONCATENADA NO LINK
    search = search_url + key1
    #######################################

    #REQUISICAO DE CONTEUDO
    try:
        searc = requests.get(search)
    except:
        return False

    webpage = html.fromstring(searc.content)
    href = webpage.xpath('//a/@href')
    #print(href)
    conca = str(href[23]) + "?ref=tpl1"
    print(href[23])
    tena = "http://www.theplantlist.org"
    concatena = tena + conca  
    print(concatena)
    content = requests.get(concatena).content
    ######################################

    #BS4 ORGANIZACAO
    soup = BeautifulSoup(content, "lxml")
    print("Aguarde o Carregamento = #_________")
########################################################################
########## FILTRAGEM DOS DADOS #########################################


    text = soup.get_text()
    text = text.replace("  "," ")

    #print (text)

    ipitudo = text # sera usado pelo ipni
    #print(text)

    print (text)

    sino = []
    acum = {}
    i = 0

    while (acum != "Date supplied"):
        #print (acum)
        acum = text[i:i+13]
        #print (acum)
        i+=1
        if (i > len(text)):
            break
    print(acum)   
    sino = text[i+12:]
    #print (sino)
    final = []
    acuma = {}
    j = 0
    while (acuma != "tplTableInit"):
        print(".")
        acuma = sino[j:j+12]
        j+=1
        if (j > len(sino)):
            break
    print (acuma)
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
    print (resultante )       
    print("Aguarde o Carregamento = ###_______")
    #print(resultante)
############################## Busca pelo link IPNI

    auxiliar = ipitudo[0:6]
    print (auxiliar)
    #print (auxiliar)
    p = 0
    while auxiliar != 'IPNI: ':
        #print (auxiliar)
        p+=1
        auxiliar = ipitudo[p:p+6]
    halfinipini = ipitudo[p+6:]
    if auxiliar != "IPNI: ":
        return resultante
    m = 0
    auxpini = ''
    print("Aguarde o Carregamento = ####______")
    while ((auxpini != '.\nSynonyms') or (auxpini != 'Earlier ve')):
        #print (auxpini)
        m+=1
        auxpini = halfinipini[m:m+10]
    
    linkipnifinal = halfinipini[:m]

    print (linkipnifinal)
    ############################## Besca pelo id do autor
    searcipini = requests.get(linkipnifinal).content

    soupin = BeautifulSoup(searcipini, "lxml")

    print("Aguarde o Carregamento = #####_____")
    
    #textin = textin.replace("  "," ")
    #print(soupin)
    sotext = str(soupin)
    #print (sotext)
    token = {}
    l = 0
    
    while token != "urn:lsid:ipni.org:authors:":
        token = sotext[l:l+26]
        l+=1
        if l > len(sotext):
            break


    #print(sotext[l+25:])
    tokan = {}
    lk = l+25
    while tokan != " tm:":
        tokan = sotext[lk:lk+4]
        lk+=1
    #print(sotext[l+25:lk-2])
    idautor = str(sotext[l+25:lk-2])
    ###################################################
    # LINK DA PÁGINA IPINI DO AUTOR DA PLANTA
    reqautor = "http://www.ipni.org/ipni/idAuthorSearch.do?id=" + idautor + "&back_page="
    print(reqautor)
    ###################################################
    try:
        reqs = requests.get(reqautor).content
    except:
        print ("Sem nome do autor!")
        return resultante
    #print (reqs)
    soupauto = BeautifulSoup(reqs, "lxml")
    textautor = soupauto.get_text()
    #print(textautor)
    print("Aguarde o Carregamento = ########__")
    tokun = {}
    xy = 0
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
    while tokun != "Standard Form:":
        tokun = newtextautor[xy:xy+14]
        xy+=1
    textnames = newtextautor[:xy-1]

    ########### 
    textnames = textnames.replace("\n", "")
    textnames = textnames.replace("\t", "")
    textnames = textnames.replace("  ","")
    listadenomes = textnames.split(",")
    print("Aguarde o Carregamento = #########_")
    listadenomes = set(listadenomes)

    #print (listadenomes)
    print("Aguarde o Carregamento = ##########")
    return resultante, listadenomes


########################################################################################    

     

    
final, nomesa = tpl("Hygrophila costa")
#print (final[0])
#print (nomesa)
#for i in range(len(final)):
#    print (final[i])
    
