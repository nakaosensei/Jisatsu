#  README 

## Instalando as dependências
### Windows


##### Fazer o download do [Python 3.7](https://www.python.org/downloads/) e instalar na máquina.
![](https://imageshack.com/a/img923/4010/w5pyRE.png)


##### Abrir o *Powershell* 

Para abrir o menu especial pressione a tecla ![](https://imageshack.com/a/img923/2831/OZ2Kzy.png) + ![](https://imageshack.com/a/img924/7609/t8aqqY.png) e selecione a opção:


![](https://imageshack.com/a/img922/8240/7PAg3f.png)

##### Acessando a pasta para instalação das dependências: 
na janela do *Powershell* digite o comando 

	> cd C:\Users\SuaPastadeUsuário\AppData\Local\Programs\Python\Python37*\Scripts




Exemplo:

![](https://imageshack.com/a/img921/930/910rrP.png)

Feito isso executar os seguintes comandos:

	> pip install --upgrade pip
	> pip install --upgrade pip wheel setuptools
	> pip install python-csv
	> pip install docutils pygments pypiwin32 kivy.deps.sdl2 kivy.deps.glew
	> pip install kivy.deps.gstreame
	> pip install kivy.deps.angle
	> pip install kivy
	> pip install python-csv
	> pip install requests
	> pip install bs4
	> pip install pandas

##### Agora é só fazer o download do programa [nesse link](https://github.com/nakaosensei/Jisatsu.git) e extrair o arquivo na sua unidade raiz.



## Para Abrir a Interface

Com o terminal no diretório da pasta  **\Jisatsu\scripts\coletas** execute o seguinte comando:

	cd C:\Jisatsu\scripts\coletas 
	C:\Jisatsu\scripts\coletas# > python3 main.py
<br>



## Interface

### Carregando a Lista de Nomes:

![enter image description here](https://imageshack.com/a/img923/4456/1dDGzm.png)



### Selecionando o Xlsx
![enter image description here](https://imageshack.com/a/img921/3194/lFd18A.png)



### Sincronizar Base de Dados

Esse botão executa a busca nos 4 sites e grava elas no banco de dados. Um pouco de paciência nessa parte, pois pode demorar em média 1min a 5min por nomes na lista, devido ao número de ocorrências geralmente ser grande. Após clicar em sincronizar, aguarde até que o botão volte a ficar cinza.

![enter image description here](https://imageshack.com/a/img923/5307/FEqB1s.png)



<br>

### Gerar Tabelas Xlsx

Com a planilha de nomes já carregada, basta clicar em um dos botões para gerar as planilhas de resultados obtidos.
Temos três opções de planilha:

1. Gerar planilha de comparação dos nomes no Flora do Brasil e The Plant List.
2. Gerar planilha dos nomes certos e sinônimos.
3. Gerar planilha de ocorrências encontradas.

As planilhas são geradas de imediato na mesma pasta **\Jisatsu\scripts\coletas** . 

![enter image description here](https://imageshack.com/a/img922/3391/Q4FrwW.png)








