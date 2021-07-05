import unittest

from SentiNet.SentiLiteralNet import SentiLiteralNet

class SentiLiteralNetTest(unittest.TestCase):

    def setUp(self) -> None:
        self.sentiNet = SentiLiteralNet("../turkish_sentiliteralnet.xml")

    def test_getPositives(self):
        self.assertEquals(4335, len(self.sentiNet.getPositives()))

    def test_getNegatives(self):
        self.assertEquals(13011, len(self.sentiNet.getNegatives()))

    def test_getNeutrals(self):
        self.assertEquals(62379, len(self.sentiNet.getNeutrals()))


if __name__ == '__main__':
    unittest.main()
