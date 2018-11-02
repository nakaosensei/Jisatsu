import unittest
from FloradoBrasil.teste.teste.spiders.teste import *


class TestFlora(unittest.TestCase):

    def setUp(self):
        pass

    def test_re(self):
        self.assertTrue(TesteSpider().parse(None), 1)

