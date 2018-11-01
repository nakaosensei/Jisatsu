from bs4 import BeautifulSoup
import requests
import sys



def search_pl(gereno, especies):

    #URL DE BUSCA DO SITE
    search_url = "http://www.theplantlist.org/tpl1.1/search?q="
    ########################

    #CHAVES DE PESQUISA
    key1 = gereno
    key2 = especies
    ######################

    #STRING DE BUSCA QUE SERA CONCATENADA NO LINK
    search = search_url + key1 + "+" + key2
    #######################################

    #REQUISICAO DE CONTEUDO
    content = requests.get(search).content
    ######################################

    #BS4 ORGANIZACAO
    soup = BeautifulSoup(content, "lxml")
    #####################################

    #BUSCA DE NOMES ACEITOS DENTRO DO CONTEUDO RETORNADO
    accepted = soup.find_all("td" , class_ = "name Accepted")
    #########################################################

    #GUARDA O CONTEUDO DE ACCEPTED  EM RESULT COMO LISTA
    result = [ i.text for i in accepted]
    #####################################

    #SELECIONA APENAS OS NOMES ACEITOS
    accepted2 = soup.find_all("h1")
    for i in accepted2:
        if "accepted" in i.text.encode('utf-8'):
            result.append(i.find("span", class_ = "name").text)
    #############################################################

    # EXTRAI O "is a synonym of"
    if len(result) == 0:
        synonym = soup.find_all("span" , class_ = "subtitle")
        result = [i.text.replace("is a synonym\n of ", "") for i in synonym]
    print(result)
    return result
#########################################################################

#MANIPULACAO DOS ARQUIVOS

fname = sys.argv[1]# + ".csv"

try:
    with open(fname , "r") as fn:
        especies = []
        for line in fn:
            sp_name = line.split(",")
            sp_name[0] = sp_name[0].strip("\n").strip("\r")
            sp_name[1] = sp_name[1].strip("\n").strip("\r")
            especies.append(sp_name)
    # CRIA A LISTA DE NOMES ACEITOS
    print ("Checando nomes em The Plant List ...........")

    results = [search_pl(sp[0], sp[1]) for sp in especies]
    print ("Feito! Sinonimos encontrados.")

    # PEDE NOME DO ARQUIVO DE SAIDA E GRAVA OS NOMES ACEITOS"
    outfile = sys.argv[2] + ".csv"
    print ("Salvando resultados...")
    with open(outfile, "w") as outf:
        for sp in range(len(results)):
            outf.write(especies[sp][0] + " " + especies[sp][1])
            for x in range(len(results[sp])):
                outf.write(" " + "," + results[sp][x].encode('utf-8'))
            outf.write("\n")

    print ("Pronto! O arquivo de saida " + outfile + " esta na mesma pasta que o script")
except:
    print ("O arquivo para leitura nao foi encontrado ou as palavras contidas nele nao obtiveram resultado.")







