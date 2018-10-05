import sys
from urllib.parse import urlparse
from urllib.request import urlopen

import requests
import filer

print("Escolha o que deseja fazer")
print("Digite A para criar um diretório de trabalho")
print("Digite B para selecionar um diretório de trabalho existente")
print("Digite C para selecionar um arquivo de trabalho")
print("Digite D para sair")
input_prompt = input("Prompt")


def mkdirzao():
    x = filer.dirzao_chooser()
    filer.make_dir(x)
    return x


if input_prompt == 'A':
    mkdirzao()
elif input_prompt == 'B':
    dirzao = filer.dirzao_chooser()
elif input_prompt == 'C':
    file = filer.file_chooser()
elif input_prompt == 'D':
    sys.exit()




#saite = "http://www.theplantlist.org/tpl1.1/search?q=elodea&csv=true" QUASE
#r = requests.get(saite, True) LÁ
#print(r.content) VAMO COM CALMA
