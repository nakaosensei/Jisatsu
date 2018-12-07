import unittest

from tpl.TPLrefatorado.tplrefat import construUrl, requisicaoTPL1, procuraHref, requestHref, trataHref, encontraSinonimos, encontraSinonimos2, idIpiniAutor

class testPlantList(unittest.TestCase):


    def testConstruUrl(self):
        self.assertEqual(construUrl('Macrochloa'), 'http://www.theplantlist.org/tpl1.1/search?q=Macrochloa')

    def testRequisicaoTPL1(self):
        self.assertTrue(requisicaoTPL1('http://www.theplantlist.org/tpl1.1/search?q=Macrochloa'),)
        self.assertFalse(requisicaoTPL1('http://www.theplantlist.org/tpl1.1/search?q=Macroc'),)

    def testProcuraHref(self):
        self.assertTrue(procuraHref(requisicaoTPL1('http://www.theplantlist.org/tpl1.1/search?q=Macrochloa')))
        self.assertFalse(procuraHref(requisicaoTPL1('http://www.theplantlist.org/tpl1.1/search?q=Macra')))

    def testRequestHref(self):
        self.assertTrue(requestHref(procuraHref(requisicaoTPL1('http://www.theplantlist.org/tpl1.1/search?q=Macrochloa'))))
        self.assertFalse(requestHref(procuraHref(requisicaoTPL1('http://www.theplantlist.org/tpl1.1/search?q=Macroc'))))

    def testTratref(self):
        self.assertTrue(trataHref(requestHref(procuraHref(requisicaoTPL1('http://www.theplantlist.org/tpl1.1/search?q=Macrochloa')))))
        self.assertFalse(trataHref(requestHref(procuraHref(requisicaoTPL1('http://www.theplantlist.org/tpl1.1/search?q=Macr')))))

    def testEcontraSinonimos(self):
        self.assertFalse(encontraSinonimos(" "))

    def testEcontraSinonimos2(self):
        self.assertFalse(encontraSinonimos(" "))

    def testIdAuthor(self):
        self.assertFalse(idIpiniAutor("John"))