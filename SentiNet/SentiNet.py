import pkg_resources

from SentiNet.PolarityType import PolarityType
from SentiNet.SentiSynSet import SentiSynSet
import xml.etree.ElementTree


class SentiNet(object):

    __senti_synset_list: dict

    def __init__(self, file_name=None):
        """
        Constructor of Turkish SentiNet. Reads the turkish_sentinet.xml file from the directory resources. For each
        sentiSynSet read, it adds it to the sentiSynSetList.
        """
        self.__senti_synset_list = {}
        if file_name is None:
            file_name = pkg_resources.resource_filename(__name__, 'data/turkish_sentinet.xml')
        root = xml.etree.ElementTree.parse(file_name).getroot()
        for senti_synset in root:
            _id = ""
            positive_score = 0.0
            negative_score = 0.0
            for part in senti_synset:
                if part.tag == "ID":
                    _id = part.text
                else:
                    if part.tag == "PSCORE":
                        positive_score = part.text
                    else:
                        negative_score = part.text
            if _id != "":
                self.__senti_synset_list[_id] = SentiSynSet(_id, positive_score, negative_score)

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
        return self.__senti_synset_list[_id]

    def addSentiSynSet(self, senti_synset: SentiSynSet):
        """
        Adds specified SentiSynSet to the SentiSynSet list.

        PARAMETERS
        ----------
        senti_synset : SentiSynSet
            SentiSynSet to be added
        """
        self.__senti_synset_list[senti_synset.getId()] = senti_synset

    def removeSentiSynSet(self, senti_synset: SentiSynSet):
        """
        Removes specified SentiSynSet from the SentiSynSet list.

        PARAMETERS
        ----------
        senti_synset : SentiSynSet
            SentiSynSet to be removed
        """
        del self.__senti_synset_list[senti_synset.getId()]

    def getPolarity(self, polarity_type: PolarityType) -> list:
        """
        Constructs and returns a list of ids, which are the ids of the SentiSynSets having polarity
        polarityType.

        PARAMETERS
        ----------
        polarity_type : PolarityType
            PolarityTypes of the searched SentiSynSets

        RETURNS
        -------
        list
            A list of id having PolarityType polarityType.
        """
        result = []
        for sentiSynSet in self.__senti_synset_list.values():
            if sentiSynSet.getPolarity() == polarity_type:
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
        return self.getPolarity(PolarityType.POSITIVE)

    def getNegatives(self) -> list:
        """
        Returns the ids of all negative SentiSynSets.

        RETURNS
        -------
        list
            A list of ids of all negative SentiSynSets.
        """
        return self.getPolarity(PolarityType.NEGATIVE)

    def getNeutrals(self) -> list:
        """
        Returns the ids of all neutral SentiSynSets.

        RETURNS
        -------
        list
            A list of ids of all neutral SentiSynSets.
        """
        return self.getPolarity(PolarityType.NEUTRAL)

    def saveAsXml(self, file_name: str):
        """
        Method to write SynSets to the specified file in the XML format.

        PARAMETERS
        ----------
        file_name : str
            file name to write XML files
        """
        outfile = open(file_name, 'w', encoding='utf8')
        outfile.write("<SYNSETS>\n")
        for synSet in self.__senti_synset_list.values():
            synSet.saveAsXml(outfile)
        outfile.write("</SYNSETS>\n")
        outfile.close()
