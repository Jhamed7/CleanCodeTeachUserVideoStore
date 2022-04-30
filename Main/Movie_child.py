from Main.Movie import Movie


class MovieChild(Movie):
    def determine_amount(self, daysrented):
        if daysrented > 3:
            return 1.5 + (daysrented - 3) * 1.5
        return 1.5

    def frequent_rental_point(self, getDaysRented):
        _frequentRenterPoints = 1
        if self.getPriceCode() == Movie.NEW_RELEASE and getDaysRented > 1:
            _frequentRenterPoints = 2
        return _frequentRenterPoints
