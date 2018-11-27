import unittest
from decoder import Decoder

class TestsDecoder(unittest.TestCase):

    def testDecode(self):
        decod = Decoder()
        f = open("outSpecies.txt","r")
        testStr = f.read()
        f.close()
        manager = decod.decode(testStr)
        for oc in manager.ocurrences:
            self.ocurrence = [oc.plant,oc.owner,oc.locationDesc,oc.country,oc.state,oc.city,oc.latitude,oc.longitude,oc.dataColeta,oc.resource]
            self.testManagerDecode()


    def testGetStringsBetween(self):
        decod = Decoder()
        self.list = decod.getStringsBetween("a vida e bela","vida","bela")
        self.testStringList()

    def testGetStringBetweenS(self):
        decod = Decoder()
        self.out = decod.getStringsBetweenS("a vida e bela","vida","bela")
        self.assertEqual(" e ", self.out)


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

    def testManagerDecode(self):
        if not hasattr(self, 'ocurrence'):
            self.ocurrence=[]
        forbiddenChars = ['>','<']
        for atrib in self.ocurrence:
            for i in range(0,len(atrib)):
                self.assertNotIn(atrib[i],forbiddenChars)


    if __name__=='__main__':
        unittest.main()
