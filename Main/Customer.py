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

    def statement_header(self):
        return f"Rental Record for {self.getName()}" + "\n"

    def statement_body(self, _frequentRenterPoints, _result, _totalAmount):
        for rental in self.rentals:
            _thisAmount = 0
            _thisAmount = rental.determine_amount()

            _frequentRenterPoints += rental.frequent_rental_point()
            _totalAmount += _thisAmount
            _result = self.format_footer(_result, _thisAmount, rental)
        return _frequentRenterPoints, _result, _totalAmount



    def statement_footer(self, _frequentRenterPoints, _result, _totalAmount):
        _result += "You owed " + "{:.1f}".format(_totalAmount) + "\n"
        _result += f"You earned {str(_frequentRenterPoints)}" + " frequent renter points\n"

        return _result

    def format_footer(self, _result, _thisAmount, rental):
        _result += "\t" + rental.getMovie().getTitle() + "\t" + "{:.1f}".format(_thisAmount) + "\n"
        return _result
    # ----------------------------------------------------------------------------------------------------------
