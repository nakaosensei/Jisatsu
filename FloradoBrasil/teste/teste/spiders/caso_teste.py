#Para compilar: scrapy crawl teste -o teste.[formato](json, csv, xml ....)
import scrapy

class TesteSpider(scrapy.Spider):
    name = 'teste'

    def teste_request(self, nome):
        return "http://servicos.jbrj.gov.br/flora/taxon/"+nome.split(" ")[0]+"%20"+nome.split(" ")[1]

    def start_requests(self):    
        yield scrapy.Request(self.teste_request("Steinchisma decipiens"), self.parse)

    def parse(self, response):
        yield{
            'Nome': response.xpath('/html/body').extract()
        }


    