from SentiNet.SentiSynSet import SentiSynSet
from SentiNet.PolarityType import PolarityType
import xml.etree.ElementTree


class SentiNet(object):

    __sentiSynSetList: dict

    def __init__(self, fileName=None):
        """
        Constructor of Turkish SentiNet. Reads the turkish_sentinet.xml file from the resources directory. For each
        sentiSynSet read, it adds it to the sentiSynSetList.
        """
        self.__sentiSynSetList = {}
        if fileName is None:
            fileName = "turkish_sentinet.xml"
        root = xml.etree.ElementTree.parse(fileName).getroot()
        for sentiSynSet in root:
            _id = ""
            positiveScore = 0.0
            negativeScore = 0.0
            for part in sentiSynSet:
                if part.tag == "ID":
                    _id = part.text
                else:
                    if part.tag == "PSCORE":
                        positiveScore = part.text
                    else:
                        negativeScore = part.text
            if _id != "":
                self.__sentiSynSetList[_id] = SentiSynSet(_id, positiveScore, negativeScore)

    def getSentiSynSet(self, _id: str) -> SentiSynSet:
        """
        Accessor for a single SentiSynSet.

        PARAMETERS
        ----------
        _id : str
            Id of the searched SentiSynSet.

        RETURNS
        -------
        SentiSynSet
            SentiSynSet with the given id.
        """
        return self.__sentiSynSetList[_id]

    def addSentiSynSet(self, sentiSynSet: SentiSynSet):
        """
        Adds specified SentiSynSet to the SentiSynSet list.

        PARAMETERS
        ----------
        sentiSynSet : SentiSynSet
            SentiSynSet to be added
        """
        self.__sentiSynSetList[sentiSynSet.getId()] = sentiSynSet

    def removeSentiSynSet(self, sentiSynSet: SentiSynSet):
        """
        Removes specified SentiSynSet from the SentiSynSet list.

        PARAMETERS
        ----------
        sentiSynSet : SentiSynSet
            SentiSynSet to be removed
        """
        del self.__sentiSynSetList[sentiSynSet.getId()]

    def getPolarity(self, polarityType: PolarityType.PolarityType) -> list:
        """
        Constructs and returns a list of ids, which are the ids of the SentiSynSets having polarity
        polarityType.

        PARAMETERS
        ----------
        polarityType : PolarityType
            PolarityTypes of the searched SentiSynSets

        RETURNS
        -------
        list
            A list of id having polarityType polarityType.
        """
        result = []
        for sentiSynSet in self.__sentiSynSetList.values():
            if sentiSynSet.getPolarity() == polarityType:
                result.append(sentiSynSet.getId())
        return result

    def getPositives(self) -> list:
        """
        Returns the ids of all positive SentiSynSets.

        RETURNS
        -------
        list
            A list of ids of all positive SentiSynSets.
        """
        return self.getPolarity(PolarityType.PolarityType.POSITIVE)

    def getNegatives(self) -> list:
        """
        Returns the ids of all negative SentiSynSets.

        RETURNS
        -------
        list
            A list of ids of all negative SentiSynSets.
        """
        return self.getPolarity(PolarityType.PolarityType.NEGATIVE)

    def getNeutrals(self) -> list:
        """
        Returns the ids of all neutral SentiSynSets.

        RETURNS
        -------
        list
            A list of ids of all neutral SentiSynSets.
        """
        return self.getPolarity(PolarityType.PolarityType.NEUTRAL)

    def saveAsXml(self, fileName: str):
        """
        Method to write SynSets to the specified file in the XML format.

        PARAMETERS
        ----------
        fileName : str
            file name to write XML files
        """
        outfile = open(fileName, 'w', encoding='utf8')
        outfile.write("<SYNSETS>\n")
        for synSet in self.__sentiSynSetList.values():
            synSet.saveAsXml(outfile)
        outfile.write("</SYNSETS>\n")
        outfile.close()
