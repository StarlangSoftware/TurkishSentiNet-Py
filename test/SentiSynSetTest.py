import unittest

from SentiNet.SentiNet import SentiNet


class SentiSynSetTest(unittest.TestCase):

    def setUp(self) -> None:
        self.sentiNet = SentiNet("../SentiNet/data/turkish_sentinet.xml")

    def test_saveAsXml(self):
        outFile = open("test.xml", "w")
        sentiSynSet = self.sentiNet.getSentiSynSet("TUR10-1093230")
        sentiSynSet.saveAsXml(outFile)
        sentiSynSet = self.sentiNet.getSentiSynSet("TUR10-0730690")
        sentiSynSet.saveAsXml(outFile)
        sentiSynSet = self.sentiNet.getSentiSynSet("TUR10-0969360")
        sentiSynSet.saveAsXml(outFile)
        outFile.close()
        input = open("test.xml", "r")
        line = input.readline()
        self.assertEquals("<SYNSET><ID>TUR10-1093230</ID><PSCORE>0.25</PSCORE><NSCORE>0.0</NSCORE></SYNSET>\n", line)
        line = input.readline()
        self.assertEquals("<SYNSET><ID>TUR10-0730690</ID><PSCORE>0.0</PSCORE><NSCORE>0.0</NSCORE></SYNSET>\n", line)
        line = input.readline()
        self.assertEquals("<SYNSET><ID>TUR10-0969360</ID><PSCORE>0.0</PSCORE><NSCORE>1.0</NSCORE></SYNSET>\n", line)
        input.close()


if __name__ == '__main__':
    unittest.main()
