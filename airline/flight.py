from airline.seat import Seat

class Flight(object):
    """
    A Flight is a flight number and all its associated seats
    """

    six_seats = [ "A", "B", "C", "D", "E", "F"]

    def __init__(self, flight_no: str, seat_rows: int, seat_letters: list):

        self._seats = []
        self._flight_no = flight_no
        self._seat_rows = seat_rows
        self._seat_letters = seat_letters

        for i in range(1, seat_rows + 1):
            for l in seat_letters:
                self._seats.append(Seat(flight_no, "{}{}".format(i, l)).dict())

    def flight_no(self):
        return self._flight_no

    def dict(self):
        return self._seats
