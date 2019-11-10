from SentiNet import PolarityType


class SentiSynSet(object):

    __id: str
    __positiveScore: float
    __negativeScore: float

    """
    Constructor of SentiSynSet. Gets input id, positiveScore, negativeScore and sets all corresponding attributes.

    PARAMETERS
    ----------
    id : str
        Id of the SentiSynSet.
    positiveScore : float
        Positive score of the SentiSynSet.
    negativeScore : float
        Negative score of the SentiSynSet.
    """
    def __init__(self, id: str, positiveScore: float, negativeScore: float):
        self.__id = id
        self.__positiveScore = positiveScore
        self.__negativeScore = negativeScore

    """
    Accessor for the positiveScore attribute.
    
    RETURNS
    -------
    float
        PositiveScore of the SentiSynSet.
    """
    def getPositiveScore(self) -> float:
        return self.__positiveScore

    """
    Accessor for the negativeScore attribute.
    
    RETURNS
    -------
    float
        NegativeScore of the SentiSynSet.
    """
    def getNegativeScore(self) -> float:
        return self.__negativeScore

    """
    Accessor for the id attribute.
    
    RETURNS
    -------
    str
        Id of the SentiSynSet.
    """
    def getId(self) -> str:
        return self.__id

    """
    Returns the polarityType of the sentiSynSet. If the positive score is larger than the negative score, the polarity 
    is positive; if the negative score is larger than the positive score, the polarity is negative; if both positive
    score and negative score are equal, the polarity is neutral.
    
    RETURNS
    -------
    PolarityType
        PolarityType of the sentiSynSet.
    """
    def getPolarity(self) -> PolarityType.PolarityType:
        if self.__positiveScore > self.__negativeScore:
            return PolarityType.PolarityType.POSITIVE
        else:
            if self.__positiveScore < self.__negativeScore:
                return PolarityType.PolarityType.NEGATIVE
            else:
                return PolarityType.PolarityType.NEUTRAL

    """
    Method to write SynSets to the specified file in the XML format.

    PARAMETERS
    ----------
    outfile : file 
        File to write XML files
    """
    def saveAsXml(self, outfile):
        outfile.write("<SYNSET>")
        outfile.write("<ID>" + self.__id + "</ID>")
        outfile.write("<PSCORE>" + self.__positiveScore.__str__() + "</PSCORE>")
        outfile.write("<NSCORE>" + self.__negativeScore.__str__() + "</NSCORE>")
        outfile.write("</SYNSET>\n")
