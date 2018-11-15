from lxml import html
import requests
from bs4 import BeautifulSoup
import html2text  
#######################################################################################
##################   RETORNA A LISTA DE SINÔNIMOS #####################################
def tpl(name):
    search_url = "http://www.theplantlist.org/tpl1.1/search?q="
    ########################

    #CHAVES DE PESQUISA
    key1 = name.replace(" ", "+")
    ######################

    #STRING DE BUSCA QUE SERA CONCATENADA NO LINK
    search = search_url + key1
    #######################################

    #REQUISICAO DE CONTEUDO
    searc = requests.get(search)
    webpage = html.fromstring(searc.content)
    href = webpage.xpath('//a/@href')
    conca = str(href[23]) + "?ref=tpl1"
    tena = "http://www.theplantlist.org"
    concatena = tena + conca  
    print(concatena)
    content = requests.get(concatena).content
    ######################################

    #BS4 ORGANIZACAO
    soup = BeautifulSoup(content, "lxml")

    
    text = soup.get_text()
    text = text.replace("  "," ")



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
    final =sino[:j-1].strip("\n").split('  ')

    return (final)

########################################################################################    

        

    
final = tpl("Panicum prionitis Nees")
for i in range(len(final)):
    print (final[i])
