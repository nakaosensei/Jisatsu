import unittest
from SpeciesLinkRequests import RequestMaker
from SpeciesLinkRequests import SpeciesRequest
from ocurrences import OcurrencesManager
from decoder import Decoder
class TestsSpeciesRequests(unittest.TestCase):

    def testMakeRequests(self):
        speciesRequester = RequestMaker()
        manager =speciesRequester.makeRequests('../ListaMacrofitasTests.xlsx')
        self.assertIsNotNone(manager.ocurrences)
        self.assertIsInstance(manager.ocurrences, list)
        for ocurrence in manager.ocurrences:
            self.assertIsNotNone(ocurrence.plant)


    def testMakeRequestsSingle(self):
        speciesRequester = SpeciesRequest('Dicliptera ciliaris',Decoder(),OcurrencesManager())
        manager =speciesRequester.makeRequests()
        self.assertIsInstance(manager.ocurrences, list)
        self.assertIsNotNone(manager.ocurrences)
        for ocurrence in manager.ocurrences:
            self.assertIsNotNone(ocurrence.plant)

    def testMakeRequest(self):
        speciesRequester = SpeciesRequest('Dicliptera ciliaris',Decoder(),OcurrencesManager())
        result = speciesRequester.makeRequest(100)
        self.assertIsNotNone(result)

    if __name__=='__main__':
        unittest.main()
