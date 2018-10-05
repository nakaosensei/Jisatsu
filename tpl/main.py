import sys
from urllib.parse import urlparse
from urllib.request import urlopen

import requests
import filer

print("Escolha o que deseja fazer")
print("Digite 1 para criar um diretório de trabalho")
print("Digite 2 para selecionar um diretório de trabalho existente")
print("Digite 3 para selecionar um arquivo de trabalho")
print("Digite 4 para sair")
input_prompt = input("prompt: ")

if input_prompt == 1:
    x = filer.dirzao_chooser()
    filer.make_dir(x)
elif input_prompt == 2:
    dirzao = filer.dirzao_chooser()
elif input_prompt == 3:
    file = filer.file_chooser()
elif input_prompt == 4:
    sys.exit()



#saite = "www.theplantlist.org/tpl1.1/search?q=Elodea&csv=true" ESTA
#saite = "http://www.theplantlist.org/tpl1.1/search?q=elodea&csv=true" QUASE
#r = requests.get(saite, True) LÁ
#print(r.content) VAMO COM CALMA