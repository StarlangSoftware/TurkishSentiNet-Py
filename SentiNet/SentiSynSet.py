from SentiNet.PolarityType import PolarityType


class SentiSynSet(object):

    __id: str
    __positive_score: float
    __negative_score: float

    def __init__(self, _id: str,
                 positive_score: float,
                 negative_score: float):
        """
        Constructor of SentiSynSet. Gets input id, positiveScore, negativeScore and sets all corresponding attributes.

        PARAMETERS
        ----------
        _id : str
            Id of the SentiSynSet.
        positive_score : float
            Positive score of the SentiSynSet.
        negative_score : float
            Negative score of the SentiSynSet.
        """
        self.__id = _id
        self.__positive_score = positive_score
        self.__negative_score = negative_score

    def getPositiveScore(self) -> float:
        """
        Accessor for the positiveScore attribute.

        RETURNS
        -------
        float
            PositiveScore of the SentiSynSet.
        """
        return self.__positive_score

    def getNegativeScore(self) -> float:
        """
        Accessor for the negativeScore attribute.

        RETURNS
        -------
        float
            NegativeScore of the SentiSynSet.
        """
        return self.__negative_score

    def getId(self) -> str:
        """
        Accessor for the id attribute.

        RETURNS
        -------
        str
            Id of the SentiSynSet.
        """
        return self.__id

    def getPolarity(self) -> PolarityType:
        """
        Returns the polarityType of the sentiSynSet. If the positive score is larger than the negative score, the
        polarity is positive; if the negative score is larger than the positive score, the polarity is negative; if
        both positive score and negative score are equal, the polarity is neutral.

        RETURNS
        -------
        PolarityType
            PolarityType of the sentiSynSet.
        """
        if self.__positive_score > self.__negative_score:
            return PolarityType.POSITIVE
        else:
            if self.__positive_score < self.__negative_score:
                return PolarityType.NEGATIVE
            else:
                return PolarityType.NEUTRAL

    def saveAsXml(self, outfile):
        """
        Method to write SynSets to the specified file in the XML format.

        PARAMETERS
        ----------
        outfile : file
            File to write XML files
        """
        outfile.write("<SYNSET>")
        outfile.write("<ID>" + self.__id + "</ID>")
        outfile.write("<PSCORE>" + self.__positive_score.__str__() + "</PSCORE>")
        outfile.write("<NSCORE>" + self.__negative_score.__str__() + "</NSCORE>")
        outfile.write("</SYNSET>\n")

    def __repr__(self):
        return f"{self.__id} {self.__positive_score} {self.__negative_score}"
