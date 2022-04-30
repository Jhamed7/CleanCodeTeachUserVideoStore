class Movie:
    CHILDRENS = 2
    REGULAR = 0
    NEW_RELEASE = 1
    # ----------------------------------------------------------------------------------------------------------

    # _title=""
    # _priceCode=0
    # ----------------------------------------------------------------------------------------------------------

    def __init__(self,title,priceCode):
         self._title = title
         self._priceCode = priceCode

    # ----------------------------------------------------------------------------------------------------------

    def getPriceCode(self):
        return self._priceCode
    # ----------------------------------------------------------------------------------------------------------

    def setPriceCode(self,code):
        self._priceCode = code
    # ----------------------------------------------------------------------------------------------------------

    def getTitle(self):
        return self._title
    # ----------------------------------------------------------------------------------------------------------
    def determine_amount(self, daysrented):
        _thisAmount = 0
        if self.getPriceCode() == Movie.REGULAR:
            _thisAmount += 2
            if daysrented > 2:
                _thisAmount += (daysrented - 2) * 1.5
        elif self.getPriceCode() == Movie.NEW_RELEASE:
            _thisAmount += daysrented * 3
        elif self.getPriceCode() == Movie.CHILDRENS:
            _thisAmount += 1.5
            if daysrented > 3:
                _thisAmount += (daysrented - 3) * 1.5
        return _thisAmount

    def frequent_rental_point(self, getDaysRented):
        _frequentRenterPoints = 1
        if self.getPriceCode() == Movie.NEW_RELEASE and getDaysRented > 1:
            _frequentRenterPoints = 2
        return _frequentRenterPoints
