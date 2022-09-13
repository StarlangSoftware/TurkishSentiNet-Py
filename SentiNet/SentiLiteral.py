from SentiNet.PolarityType import PolarityType


class SentiLiteral(object):

    __name: str
    __positive_score: float
    __negative_score: float

    def __init__(self, _name: str,
                 positive_score: float,
                 negative_score: float):
        """
        Constructor of SentiLiteral. Gets input name, positiveScore, negativeScore and sets all corresponding attributes.

        PARAMETERS
        ----------
        _name : str
            Id of the SentiLiteral.
        positive_score : float
            Positive score of the SentiLiteral.
        negative_score : float
            Negative score of the SentiLiteral.
        """
        self.__name = _name
        self.__positive_score = positive_score
        self.__negative_score = negative_score

    def getPositiveScore(self) -> float:
        """
        Accessor for the positiveScore attribute.

        RETURNS
        -------
        float
            PositiveScore of the SentiLiteral.
        """
        return self.__positive_score

    def getNegativeScore(self) -> float:
        """
        Accessor for the negativeScore attribute.

        RETURNS
        -------
        float
            NegativeScore of the SentiLiteral.
        """
        return self.__negative_score

    def getName(self) -> str:
        """
        Accessor for the name attribute.

        RETURNS
        -------
        str
            Name of the SentiLiteral.
        """
        return self.__name

    def getPolarity(self) -> PolarityType:
        """
        Returns the polarityType of the sentiLiteral. If the positive score is larger than the negative score, the
        polarity is positive; if the negative score is larger than the positive score, the polarity is negative; if
        both positive score and negative score are equal, the polarity is neutral.

        RETURNS
        -------
        PolarityType
            PolarityType of the sentiLiteral.
        """
        if self.__positive_score > self.__negative_score:
            return PolarityType.POSITIVE
        else:
            if self.__positive_score < self.__negative_score:
                return PolarityType.NEGATIVE
            else:
                return PolarityType.NEUTRAL

    def __repr__(self):
        return f"{self.__name} {self.__positive_score} {self.__negative_score}"
