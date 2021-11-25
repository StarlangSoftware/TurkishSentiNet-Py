import pkg_resources

from SentiNet.SentiLiteral import SentiLiteral
from SentiNet.PolarityType import PolarityType
import xml.etree.ElementTree


class SentiLiteralNet(object):

    __sentiLiteralList: dict

    def __init__(self, fileName=None):
        """
        Constructor of Turkish SentiNet. Reads the turkish_sentinet.xml file from the resources directory. For each
        sentiSynSet read, it adds it to the sentiLiteralList.
        """
        self.__sentiLiteralList = {}
        if fileName is None:
            fileName = pkg_resources.resource_filename(__name__, 'data/turkish_sentiliteralnet.xml')
        root = xml.etree.ElementTree.parse(fileName).getroot()
        for sentiLiteral in root:
            _name = ""
            positiveScore = 0.0
            negativeScore = 0.0
            for part in sentiLiteral:
                if part.tag == "NAME":
                    _name = part.text
                else:
                    if part.tag == "PSCORE":
                        positiveScore = part.text
                    else:
                        negativeScore = part.text
            if _name != "":
                self.__sentiLiteralList[_name] = SentiLiteral(_name, positiveScore, negativeScore)

    def getSentiLiteral(self, _name: str) -> SentiLiteral:
        """
        Accessor for a single literal.

        PARAMETERS
        ----------
        _name : str
            Name of the searched literal.

        RETURNS
        -------
        SentiLiteral
            SentiLiteral with the given name.
        """
        return self.__sentiLiteralList[_name]

    def getPolarity(self, polarityType: PolarityType) -> list:
        """
        Constructs and returns a list of ids, which are the ids of the SentiSynSets having polarity
        polarityType.

        PARAMETERS
        ----------
        polarityType : PolarityType
            PolarityTypes of the searched SentiLiterals

        RETURNS
        -------
        list
            A list of id having polarityType polarityType.
        """
        result = []
        for sentiLiteral in self.__sentiLiteralList.values():
            if sentiLiteral.getPolarity() == polarityType:
                result.append(sentiLiteral.getName())
        return result

    def getPositives(self) -> list:
        """
        Returns the ids of all positive SentiLiterals.

        RETURNS
        -------
        list
            A list of ids of all positive SentiLiterals.
        """
        return self.getPolarity(PolarityType.POSITIVE)

    def getNegatives(self) -> list:
        """
        Returns the ids of all negative SentiLiterals.

        RETURNS
        -------
        list
            A list of ids of all negative SentiLiterals.
        """
        return self.getPolarity(PolarityType.NEGATIVE)

    def getNeutrals(self) -> list:
        """
        Returns the ids of all neutral SentiLiterals.

        RETURNS
        -------
        list
            A list of ids of all neutral SentiLiterals.
        """
        return self.getPolarity(PolarityType.NEUTRAL)
