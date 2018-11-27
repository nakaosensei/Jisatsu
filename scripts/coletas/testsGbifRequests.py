import unittest
from GbifRequests import GbifRequests

class TestsGbifRequests(unittest.TestCase):

    def testmakeRequests(self):
        gbifRequester = GbifRequests()
        manager = gbifRequester.makeRequests('../ListaMacrofitasTests.xlsx')
        self.assertIsNotNone(manager.ocurrences)
        self.assertIsInstance(manager.ocurrences, list)
        for ocurrence in manager.ocurrences:
            self.assertIsNotNone(ocurrence.plant)

    def testSearchIds(self):
        gbifRequester = GbifRequests()
        results = gbifRequester.searchIDS('Hygrophila guianensis Nees')
        self.assertIsNotNone(results)

    def testGetOccurrencesFromSpecies(self):
        gbifRequester = GbifRequests()
        results = gbifRequester.searchIDS('Hygrophila guianensis Nees')
        for ocurrence in results:
            self.assertIsNotNone(ocurrence)

    if __name__=='__main__':
        unittest.main()
