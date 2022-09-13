import pkg_resources

from SentiNet.SentiLiteral import SentiLiteral
from SentiNet.PolarityType import PolarityType
import xml.etree.ElementTree


class SentiLiteralNet(object):

    __senti_literal_list: dict

    def __init__(self, file_name=None):
        """
        Constructor of Turkish SentiNet. Reads the turkish_sentinet.xml file from the resources directory. For each
        sentiSynSet read, it adds it to the sentiLiteralList.
        """
        self.__senti_literal_list = {}
        if file_name is None:
            file_name = pkg_resources.resource_filename(__name__, 'data/turkish_sentiliteralnet.xml')
        root = xml.etree.ElementTree.parse(file_name).getroot()
        for senti_literal in root:
            _name = ""
            positive_score = 0.0
            negative_score = 0.0
            for part in senti_literal:
                if part.tag == "NAME":
                    _name = part.text
                else:
                    if part.tag == "PSCORE":
                        positive_score = part.text
                    else:
                        negative_score = part.text
            if _name != "":
                self.__senti_literal_list[_name] = SentiLiteral(_name,
                                                                positive_score,
                                                                negative_score)

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
        return self.__senti_literal_list[_name]

    def getPolarity(self, polarity_type: PolarityType) -> list:
        """
        Constructs and returns a list of ids, which are the ids of the SentiSynSets having polarity
        polarityType.

        PARAMETERS
        ----------
        polarity_type : PolarityType
            PolarityTypes of the searched SentiLiterals

        RETURNS
        -------
        list
            A list of id having polarityType polarityType.
        """
        result = []
        for senti_literal in self.__senti_literal_list.values():
            if senti_literal.getPolarity() == polarity_type:
                result.append(senti_literal.getName())
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
