#Para compilar: scrapy crawl teste -o teste.[formato](json, csv, xml ....)
import unittest
import scrapy
import openpyxl

class TesteSpider(scrapy.Spider):
	name = 'teste'
	
	def start_requests(self):	
		dado = openpyxl.load_workbook('ListaMacrofitas.xlsx')
		planilha = dado.sheetnames[0]
		sheet = dado[planilha]
		pesquisa = []

		for row in sheet['A1:A1048576']:
			for cell in row:
				if cell.value is None:
					break
				nome = cell.value
				nome = nome.split(" ")
				pesquisa.append(nome[0]+"%20"+nome[1])

		for nome in pesquisa:
			yield scrapy.Request("http://servicos.jbrj.gov.br/flora/taxon/{}".format(nome), self.parse)
	
	def parse(self, response):
		yield{
			'Nome': response.xpath('/html/body').extract()
		}			
