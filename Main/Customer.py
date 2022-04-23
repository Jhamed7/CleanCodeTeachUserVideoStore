from Main.Movie import Movie


class Customer:
    # _name = ""
    # _rentals = []

    # ----------------------------------------------------------------------------------------------------------

    # default constructor
    def __init__(self, name):
        self.name = name
        self.rentals=[]

    # ----------------------------------------------------------------------------------------------------------

    def addRental(self, rental):
        self.rentals.append(rental)

    # ----------------------------------------------------------------------------------------------------------

    def getName(self):
        return self.name

    # ----------------------------------------------------------------------------------------------------------

    def statement(self):
        _totalAmount = 0
        _frequentRenterPoints = 0
        _result = self.statement_header()
        _frequentRenterPoints, _result, _totalAmount = self.statement_body(_frequentRenterPoints, _result, _totalAmount)

        _result = self.statement_footer(_frequentRenterPoints, _result, _totalAmount)

        return _result

    def statement_footer(self, _frequentRenterPoints, _result, _totalAmount):
        _result += "You owed " + "{:.1f}".format(_totalAmount) + "\n"
        _result += f"You earned {str(_frequentRenterPoints)}" + " frequent renter points\n"

        return _result

    def statement_body(self, _frequentRenterPoints, _result, _totalAmount):
        for rental in self.rentals:
            _thisAmount = 0
            # determines the amount for each line
            if rental.getMovie().getPriceCode() == Movie.REGULAR:
                _thisAmount += 2
                if rental.getDaysRented() > 2:
                    _thisAmount += (rental.getDaysRented() - 2) * 1.5
            elif rental.getMovie().getPriceCode() == Movie.NEW_RELEASE:
                _thisAmount += rental.getDaysRented() * 3
            elif rental.getMovie().getPriceCode() == Movie.CHILDRENS:
                _thisAmount += 1.5
                if rental.getDaysRented() > 3:
                    _thisAmount += (rental.getDaysRented() - 3) * 1.5

            _frequentRenterPoints += 1
            if rental.getMovie().getPriceCode() == Movie.NEW_RELEASE and rental.getDaysRented() > 1:
                _frequentRenterPoints += 1
            _result += "\t" + rental.getMovie().getTitle() + "\t" + "{:.1f}".format(_thisAmount) + "\n"
            _totalAmount += _thisAmount
        return _frequentRenterPoints, _result, _totalAmount

    def statement_header(self):
        return f"Rental Record for {self.getName()}" + "\n"
    # ----------------------------------------------------------------------------------------------------------
