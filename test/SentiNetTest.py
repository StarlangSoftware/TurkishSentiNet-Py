import unittest

from SentiNet.SentiNet import SentiNet


class SentiNetTest(unittest.TestCase):

    def setUp(self) -> None:
        self.sentiNet = SentiNet("../turkish_sentinet.xml")

    def test_getPositives(self):
        self.assertEquals(3100, len(self.sentiNet.getPositives()))

    def test_getNegatives(self):
        self.assertEquals(10191, len(self.sentiNet.getNegatives()))

    def test_getNeutrals(self):
        self.assertEquals(63534, len(self.sentiNet.getNeutrals()))


if __name__ == '__main__':
    unittest.main()
