import unittest

from scripts.gbif import *
from scripts.gbif.GbifRequests import *


class TestGbiff(unittest.TestCase):

    def setUp(self):
        pass

    def test_g(self):
        self.assertEqual(len(GbifRequests.searchID(None)), 1)

