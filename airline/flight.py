import string

from airline.seat import Seat

class Flight(object):
    """
    A Flight is a flight number and all its associated seats
    """

    six_seats = [ "A", "B", "C", "D", "E", "F"]

    def __init__(self, flight_no: str, seat_rows: int, seat_width: int):

        self._seats = []
        self._flight_no = flight_no
        self._seat_rows = seat_rows
        self._seat_letters = list(string.ascii_uppercase)[0:seat_width]

        for i in range(1, seat_rows + 1):
            for l in self._seat_letters:
                self._seats.append(Seat(flight_no, "{}{}".format(i, l)).dict())

    def seat_letters(self):
        return self._seat_letters

    def flight_no(self):
        return self._flight_no

    def __repr__(self):
        return '[' + ','.join(repr(i) for i in self._seats) + "]"



    def dict(self):
        return self._seats
