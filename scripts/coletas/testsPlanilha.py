import unittest
from planilha import Planilha

class TestsPlanilha(unittest.TestCase):

    def testOpenPlantXls(self):
        plants = Planilha()
        output = plants.openPlantsXls("../ListaMacrofitas.xlsx")
        self.list=output
        self.testStringList()

        self.list = plants.reducePlants(output)
        self.testStringList()

    def testChangeWeirdChars(self):
        plants = Planilha()
        output = plants.openPlantsXls("../ListaMacrofitas.xlsx")
        self.list = plants.changeWeirdChars(output)
        self.testStringList()

    def testListStartsWith(self):
        plants = Planilha()
        output = plants.openPlantsXls("../ListaMacrofitas.xlsx")
        self.list = plants.changeWeirdChars(output)
        self.testStringList()

    def testReducePlants(self):
        plants = Planilha()
        output = plants.openPlantsXls("../ListaMacrofitas.xlsx")
        self.list = plants.reducePlants(output)
        self.testStringList()

    def testStringList(self):
        if not hasattr(self, 'list'):
            self.list=[]

        forbiddenChars = ['!','%','$','¨','"','/','\\']
        for string in self.list:
            self.assertIsNotNone(string)
            self.assertIsInstance(string,str)
            if type(string) is str:
                for i in range(0,len(string)):
                    self.assertNotIn(string[i],forbiddenChars)

    if __name__=='__main__':
        unittest.main()
