# The Jisatsu project

# Objetivos
Jisatsu é um projeto que tem por objetivo o mapeamento da localidade de plantas registradas em diversas bases de dados no mundo. Esse trabalho faz parte de uma pesquisa de pós doutorado da Universidade Estadual de Maringá com o apoio de acadêmicos da UTFPR-cm, temos quatro ciclos de desenvolvimento, e em cada ciclo temos que atingir o objetivo descrito abaixo.  
- Coletar dados de diversas bases de dados relacionadas à plantas Macrófitas.
- Normalização dos dados coletados.
- Classificar corretamente as diversas espécies de plantas coletadas nas bases por localidade.
- Gerar visualizações para os resultados obtidos.

# Situação atual e justificativa do projeto
- O estudo de elementos da flora está intimamente ligado com a história da humanidade, a descoberta e registro de novas espécies é algo que nos fascina há tempos, por essa razão, sabemos que informações espaço/temporais dessas descobertas estão espalhadas em diversas bases de dados hoje, e por isso visamos realizar a coleta e um mapeamento global para que estudos posteriores tenham essa informação concreta.
- A necessidade desse trabalho surgiu da tese de pós doutorado da aluna Tânia da Silva Sauro, orientanda da doutora Karina dos ventos estridentes. Além de cooperarmos com um projeto de pesquisa real, o produto desse projeto será utilizado como nota para a disciplina Engenharia de Software 2. 

# Objetivos SMART e critérios de sucesso do projeto
- Validar os nomes das espécies das macrófitas que estão na lista fornecida pelo cliente baseando na base de dados da Flora do Brasil e do The Plant List. 
- Extrair os seguintes dados de cada espécie validada: classe, família, tribo, forma de vida, substrato, origem, endemismo e distribuição geográfica.
- Buscar as ocorrências das espécies validadas nas plataformas Specieslink e GBIF.

# EAP
Segue a Estrutura Analítica do Projeto, o projeto contém quatro etapas principais, sendo o Gerenciamento do projeto, coleta de dados, normalização e exportação para xls, o trabalho está dividido na imagem abaixo.

![EAP completa](https://i.imgur.com/lV7egCx.jpg)


# Principais requisitos das principais entregas/produtos

## Requisitos funcionais
Os dados das coletas das plantas não podem ser duplicados.
Devem estar presentes o autor e a localização para cada planta encontrada na américa do sul, em uma tabela do .xls.


# Marcos
|    Fases      |  Marcos  | Previsão |
|---------------|----------|----------|
| Iniciação     | Projeto aprovado                            |   07/09/2018   |
| Planejamento  | Plano de Gerenciamento de Projetos Aprovado |   21/09/2018   |
| Entrega 1     | Termo de abertura, Documentação do gerenciamento de escopo e tempo         |   21/09/2018   |
| Entrega 2     | Dados Gbif coletados   |   05/10/2018   |
| Entrega 3     | Species Link coletados    |   19/11/2018   |
| Encerramento  | Normalização e Exportação para XLS         |   06/12/2018, 07/12/2018   |


# Partes Interessadas
## Informações de Identificação
 * Tania 
  > Cliente 
  > taniacrivelari@hotmail.com 

 * Karina 
  > Cliente 
  > karina.fidanza@gmail.com 

 * Thiago Alexandre Nakao França 
  > Desenvolvedor
  > nakaosensei@gmail.com 

 * Higor Luiz Farinha Celante 
  > Desenvolvedor 
  > higor.celante@gmail.com 

 * Thiago Alexsander da Costa Pereira
  > Desenvolvedor
  > thiago.2014@alunos.utfpr.edu.br

 * Érica Yurie Saito 
  > Gerente de Projeto 
  > ericasaito@alunos.utfpr.edu.br 

 * Reginaldo Ré 
  > Avaliador do Projeto
  > reginaldo.re@utfpr.edu.br
		 
## Informações de avaliação
* Requisitos Essenciais
> O sistema deve extratir os registros de plantas macrófitas coletadas na américa do sul, ultilizando-se de dados disponíveis nos domínios Gbif e SpeciesLink. 		
O sistema deve normalizar as macrófitas coletadas utilizando como base dados extraídos dos domínios PlantList e FloraDoBrasil.
* Principais Expectativas
> No Processo de normalização, cada espécie deverá estar listada com o nome de espécie atualmente correto, juntamente com o nome do autor correspondente, sua respectiva coordenada geográfica e adicionalmente deve-se ter um histórico de nomes de espécies anteriores. 
* Influência Potencial no Projeto
> Súbita mudança nos requisitos.
> Queda em alguns dos domínios de interesse.
* Fase de Maior Interesse no Ciclo de Vida
>Coleta de Requisitos 
## Classificação das partes interessadas:
* Interna 
 
  - Higor Celante
  - Thiago Nakao
  - Thiago Pereira
  - Erica Saito

* Externa
  - Carina
  - Tânia
  - Comunidade Acadêmica Ambiental	

* Apoiador 
  - Reginaldo Ré

# Restrições
## Data da entrega.
* Após a data do término do projeto, será tarde demais para entregar a ferramenta.
## Tempo de desenvolvimento.
* Por ser um projeto desenvolvido por alunos, o tempo dedicado ao desenvolvimento da ferramenta é limitado.
	

# Premissas
- Os nomes das macrófitas que serão validadas estão presentes no banco de dados da Flora do Brasil, do The Plant List. 
- Os dados das macrófitas que serão validadas estão presentes na plataforma Specieslink e GBIF.

# Riscos
- Surgimento de muitos dados incoerêntes na coleta.
- Subita queda nos serviços do Gbif, Species Link, Floradobrasil e PlantList.
- Problemas na normalização duplicada de instâncias cruzadas com nomes diferentes entre o Gbif e SpeciesLink.
- Assumir podas de espécies duvidosas na normalização que não poderiam ter sido descartadas.

# Referencias
- [GBIF](https://www.gbif.org/)
- [Species Link](http://www.splink.cria.org.br/)
- [Flora do Brasil](http://floradobrasil.jbrj.gov.br/)
- [The Plant List](http://www.theplantlist.org/)

Tânia,Karina-orientadora,daiane barueri(espécies de peixes)

