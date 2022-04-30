from Main.Movie import Movie

class Rental:

    def __init__(self,movie, daysRented):
        self._movie = movie
        self._daysRented = daysRented
    # ----------------------------------------------------------------------------------------------------------

    def getDaysRented(self):
        return self._daysRented
    # ----------------------------------------------------------------------------------------------------------

    def getMovie(self):
        return self._movie

    def determine_amount_rental(self):
        self._movie.determine_amount(self._daysRented)

    def frequent_rental_point_(self):
        self._movie.frequent_rental_point(self.getDaysRented)