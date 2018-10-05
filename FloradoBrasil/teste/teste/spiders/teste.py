#scrapy runspider teste.py -o teste1.json

import scrapy
import openpyxl

class TesteSpider(scrapy.Spider):
	name = 'teste'
	
	def start_requests(self):	
		dado = openpyxl.load_workbook('ListaMacrofitas.xlsx')
		planilha = dado.sheetnames[0]
		sheet = dado[planilha]
		pesquisa = []

		for row in sheet.iter_rows('A1:A1048576'):
			for cell in row:
				if cell.value is None:
					break
				nome = cell.value
				nome = nome.split(" ")
				pesquisa.append(nome[0]+"_"+nome[1])

		for nome in pesquisa:
			yield scrapy.Request("http://servicos.jbrj.gov.br/flora/search/{}".format(nome), self.parse)

	def parse(self, response):
		yield{
			'Nome valido': response.xpath('//*[@id="nomeCompletoTitulo"]/span').extract()
		}			
			
			
	
	


