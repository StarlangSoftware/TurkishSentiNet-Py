import unittest

from SentiNet.SentiLiteralNet import SentiLiteralNet

class SentiLiteralNetTest(unittest.TestCase):

    def setUp(self) -> None:
        self.sentiNet = SentiLiteralNet()

    def test_getPositives(self):
        self.assertEqual(4335, len(self.sentiNet.getPositives()))

    def test_getNegatives(self):
        self.assertEqual(13011, len(self.sentiNet.getNegatives()))

    def test_getNeutrals(self):
        self.assertEqual(62379, len(self.sentiNet.getNeutrals()))


if __name__ == '__main__':
    unittest.main()
