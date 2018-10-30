import requests

class requestMaker:

    def __init__(self):
        self.response = requests.post('http://www.splink.org.br/mod_perl/searchHint', data = {'ts_any':'Steinchisma laxum','offset':100})
        self.writeToFile()

    def writeToFile(self):
        file = open("generatedDocs/requestText4.json","w")
        file.write(self.response.text)
        file.close()

requester = requestMaker()
