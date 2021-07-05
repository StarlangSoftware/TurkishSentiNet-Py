from SentiNet.PolarityType import PolarityType


class SentiLiteral(object):

    __name: str
    __positiveScore: float
    __negativeScore: float

    def __init__(self, _name: str, positiveScore: float, negativeScore: float):
        """
        Constructor of SentiLiteral. Gets input name, positiveScore, negativeScore and sets all corresponding attributes.

        PARAMETERS
        ----------
        _name : str
            Id of the SentiLiteral.
        positiveScore : float
            Positive score of the SentiLiteral.
        negativeScore : float
            Negative score of the SentiLiteral.
        """
        self.__name = _name
        self.__positiveScore = positiveScore
        self.__negativeScore = negativeScore

    def getPositiveScore(self) -> float:
        """
        Accessor for the positiveScore attribute.

        RETURNS
        -------
        float
            PositiveScore of the SentiLiteral.
        """
        return self.__positiveScore

    def getNegativeScore(self) -> float:
        """
        Accessor for the negativeScore attribute.

        RETURNS
        -------
        float
            NegativeScore of the SentiLiteral.
        """
        return self.__negativeScore

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
        if self.__positiveScore > self.__negativeScore:
            return PolarityType.POSITIVE
        else:
            if self.__positiveScore < self.__negativeScore:
                return PolarityType.NEGATIVE
            else:
                return PolarityType.NEUTRAL
