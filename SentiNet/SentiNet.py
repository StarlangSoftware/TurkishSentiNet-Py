from SentiNet import SentiSynSet
from SentiNet import PolarityType
import xml.etree.ElementTree


class SentiNet(object):

    __sentiSynSetList: dict

    """
    Constructor of Turkish SentiNet. Reads the turkish_sentinet.xml file from the resources directory. For each
    sentiSynSet read, it adds it to the sentiSynSetList.
    """
    def __init__(self, fileName=None):
        self.__sentiSynSetList = {}
        if fileName is None:
            fileName = "turkish_sentinet.xml"
        root = xml.etree.ElementTree.parse(fileName).getroot()
        for sentiSynSet in root:
            id = ""
            positiveScore = 0.0
            negativeScore = 0.0
            for part in sentiSynSet:
                if part.tag == "ID":
                    id = part.text
                else:
                    if part.tag == "PSCORE":
                        positiveScore = part.text
                    else:
                        negativeScore = part.text
            if id != "":
                self.__sentiSynSetList[id] = SentiSynSet.SentiSynSet(id, positiveScore, negativeScore)

    """
    Accessor for a single SentiSynSet.
    
    PARAMETERS
    ----------
    id : str
        Id of the searched SentiSynSet.
        
    RETURNS
    -------
    SentiSynSet
        SentiSynSet with the given id.
    """
    def getSentiSynSet(self, id : str) -> SentiSynSet:
        return self.__sentiSynSetList[id]

    """
    Adds specified SentiSynSet to the SentiSynSet list.

    PARAMETERS
    ----------
    sentiSynSet : SentiSynSet
        SentiSynSet to be added
    """
    def addSentiSynSet(self, sentiSynSet : SentiSynSet):
        self.__sentiSynSetList[sentiSynSet.getId()] = sentiSynSet

    """
    Removes specified SentiSynSet from the SentiSynSet list.

    PARAMETERS
    ----------
    sentiSynSet : SentiSynSet
        SentiSynSet to be removed
    """
    def removeSentiSynSet(self, sentiSynSet : SentiSynSet):
        del self.__sentiSynSetList[sentiSynSet.getId()]

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
    def getPolarity(self, polarityType : PolarityType.PolarityType) -> list:
        result = []
        for sentiSynSet in self.__sentiSynSetList.values():
            if sentiSynSet.getPolarity() == polarityType:
                result.append(sentiSynSet.getId())
        return result

    """
    Returns the ids of all positive SentiSynSets.
    
    RETURNS
    -------
    list
        A list of ids of all positive SentiSynSets.
    """
    def getPositives(self) -> list:
        return self.getPolarity(PolarityType.PolarityType.POSITIVE)

    """
    Returns the ids of all negative SentiSynSets.

    RETURNS
    -------
    list
        A list of ids of all negative SentiSynSets.
    """

    def getNegatives(self) -> list:
        return self.getPolarity(PolarityType.PolarityType.NEGATIVE)

    """
    Returns the ids of all neutral SentiSynSets.

    RETURNS
    -------
    list
        A list of ids of all neutral SentiSynSets.
    """

    def getNeutrals(self) -> list:
        return self.getPolarity(PolarityType.PolarityType.NEUTRAL)

    """
    Method to write SynSets to the specified file in the XML format.

    PARAMETERS
    ----------
    fileName : str
        file name to write XML files
    """
    def saveAsXml(self, fileName: str):
        outfile = open(fileName, 'w')
        outfile.write("<SYNSETS>\n")
        for synSet in self.__sentiSynSetList.values():
            synSet.saveAsXml(outfile)
        outfile.write("</SYNSETS>\n")
        outfile.close()