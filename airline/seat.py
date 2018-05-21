
from datetime import datetime

class Seat(object):

    def __init__(self, flight_no, seat_no, person=None, ts=None):
        self._flight_no = flight_no
        self._seat_no   = seat_no
        if ts:
            self._ts = ts
        else:
            self._ts = datetime.utcnow()

        self._person    = person

    @staticmethod
    def make_seat( d):
        return Seat( d["flight_no"], d["seat_no"], d[ "person"], d["ts"])

    def allocate(self, person):
        self._person = person

    def deallocate(self):
        self._person = None

    def dict(self):
        return { "flight_no" : self._flight_no,
                 "seat_no"   : self._seat_no,
                 "person"    : self._person.dict(),
                 "ts"        : self._ts}
