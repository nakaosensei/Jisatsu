import requests
from bs4 import BeautifulSoup
import html2text
from Plant import Plant
from Plant import PlantsManager
import fileNk as file


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
    print (search)
    return search

def requisicaoTPL1(link,manager,nome):
    searc = requests.get(link)
    #print(searc)
    searc.encoding = 'utf-8'
    mm = searc.text
    f = file.File()
    f.writeToFile("outThePlantCru.txt",mm)

    if isAccepted(mm,manager)==1:
        print("Get inicial - Case isAccepted")
        return 1
    elif h1isSinonimoAction(mm,manager,nome)==1:
        print("Get inicial - Case sinonimo")
        return 1
    elif caseResultsTable(mm,manager,nome)==1:
        print("Get inicial - Case redirect")
        return 1
    return 0




###################################################################
####### CASO COSTATA ##############################################
#Tratar caso em que somente como o da Urochloa plantaginea, onde
#o theplantlist nao retorna uma tabela com accept e synmons, mas apenas
#um texto indicando que a planta e um sinonimo de synmons
def h1isSinonimoAction(requestStr,plantManager,nome):
    headerOnes = getStringsBetween(requestStr,"<h1>","</h1>")
    for header in headerOnes:
        if "is a <a href=\"/1.1/about/#synonym\">synonym</a>" in header:
            tmpHeader=header+"</h1>"
            originalSection=getStringsBetweenS(tmpHeader,'is a <a href="/1.1/about/#synonym">synonym</a>','</h1>')
            kewCode = getStringsBetweenS(originalSection,"<a href=\"kew-","\">")
            newLink="http://www.theplantlist.org/tpl1.1/record/kew-"+kewCode
            requisicaoTPL1(newLink,plantManager,nome)

            '''
            sinonimoPlant = getStringsBetweenS(header,'<span class="name">','is a <a href="/1.1/about/#synonym">synonym</a>')
            genusSinonimoPlant = getStringsBetweenS(sinonimoPlant,'<i class="genus">','</i>')
            speciesSinonimoPlant = getStringsBetweenS(sinonimoPlant,'<i class="species">','</i>')
            autorSinonimoPlant = getStringsBetweenS(sinonimoPlant,'<span class="authorship">','</span>')
            parsedSinonimo=genusSinonimoPlant.strip()+" "+speciesSinonimoPlant.strip()+" "+autorSinonimoPlant.strip()

            orgPlant = getStringsBetweenS(header,'is a <a href="/1.1/about/#synonym">synonym</a>','</a></span>')
            genusOrgPlant = getStringsBetweenS(orgPlant,'<i class="genus">','</i>')
            speciesOrgPlant = getStringsBetweenS(orgPlant,'<i class="species">','</i>')
            autorOrgPlant = getStringsBetweenS(orgPlant,'<span class="authorship">','</span>')
            parsedOrg=genusOrgPlant.strip()+" "+speciesOrgPlant.strip()+" "+autorOrgPlant.strip()
            print("original plant "+parsedOrg)
            print("Sinonimo plant "+parsedSinonimo)

            plantManager.addPlant(parsedOrg,autorOrgPlant,"theplantlist","nome aceito","","","","","","","","","","","")
            plantManager.addPlant(parsedSinonimo,autorSinonimoPlant,"theplantlist","sinonimo","","","","","","","","","","",parsedOrg)
            plantManager.writeAllToDb()
            '''
            return 1
    return 0


def caseResultsTable(requestStr,plantManager,nome):
    if "<h2>Results</h2>" in requestStr and "plant name records match your search criteria" in requestStr:
        result = getStringsBetweenS(requestStr,"plant name records match your search criteria","</strong>")
        result = result.replace("<strong>","")
        result = result.replace("<i>","")
        result = result.replace("</i>","")
        result = result.strip()
        if nome!=result:
            return 0
        if "<td class=\"name Accepted\">" in requestStr:
            accepteds = getStringsBetween(requestStr,"<td class=\"name Accepted\">","</td>")
            newLink = "http://www.theplantlist.org"+getStringsBetweenS(accepteds[0],"<a href='","'>")
            print(newLink)
            requisicaoTPL1(newLink,plantManager,nome)
            return 1
        elif "<td class=\"name Synonym\">" in requestStr:
            synomns = getStringsBetween(requestStr,"<td class=\"name Synonym\">","</td>")
            newLink = "http://www.theplantlist.org"+getStringsBetweenS(synomns[0],"<a href='","'>")
            print(newLink)
            requisicaoTPL1(newLink,plantManager,nome)
            return 1
        return 0

#mm = requestString que veio da requisicao get
def isAccepted(mm,plantManager):
    headerOnes = getStringsBetween(mm,"<h1>","</h1>")
    for header in headerOnes:
        if 'is an <a href="/1.1/about/#accepted">accepted' in header:
            genusSourcePlant = getStringsBetweenS(header,'<i class="genus">','</i>')
            speciesSourcePlant = getStringsBetweenS(header,'<i class="species">','</i>')
            autorSourcePlant = getStringsBetweenS(header,'<span class="authorship">','</span>')
            parsedPlant=genusSourcePlant.strip()+" "+speciesSourcePlant.strip()+" "+autorSourcePlant.strip()
            plantManager.addPlant(parsedPlant,autorSourcePlant,"theplantlist","nome aceito",'','','','','','','','','','','')
            sinonimos = getStringsBetween(mm,'<tr id=','</tr>')
            print(parsedPlant+" - "+"nome aceito")
            ###### FILTRA SINONIMOS ###############################
            fonte = 'theplantlist'
            for i in range(len(sinonimos)):
                estado = getStringsBetweenS(sinonimos[i],'<td class="name','"><a')
                genus = getStringsBetweenS(sinonimos[i],'<i class="genus">','</i>')
                species = getStringsBetweenS(sinonimos[i],'<i class="species">','</i>')
                autor = getStringsBetweenS(sinonimos[i],'<span class="authorship">','</span>')
                nome = genus.strip()+" " + species.strip() + " " + autor.strip()
                print(nome +" - sinonimo")
                plantManager.addPlant(nome.strip(),autor.strip(),fonte,"sinonimo",'','','','','','','','','','',parsedPlant)
            plantManager.writeAllToDb()
            return 1
    return 0

###############################################################################
def roda(nome):
    print("BUSCANDO PELOS SINONIMOS")
    search = construUrl(nome)
    print(" PT1/6 - OK!")
    plantManager = PlantsManager()
    searc = requisicaoTPL1(search,plantManager,nome)
    return searc

############# ate aqui igual pra todos ###############

def getStringsBetween(stringInput,startStr,endStr):
    vet = stringInput.split(startStr)
    out=[]
    for i in range(1, len(vet)):
        if endStr in vet[i]:
            vet2 = vet[i].split(endStr)
            out.append(vet2[0])
    return out

#Funcao que dado uma string de entrada e duas substrings, retorna como string
#tudo o que estiver entre elas(Se houver mais de uma ocorrencia das substrings, o resultado e acumulativo)
def getStringsBetweenS(stringInput,startStr,endStr):
    vet = stringInput.split(startStr)
    out=""
    for i in range(1, len(vet)):
        if endStr in vet[i]:
            vet2 = vet[i].split(endStr)
            out+=vet2[0]
    return out.strip()

#roda("Urochloa plantaginea")
