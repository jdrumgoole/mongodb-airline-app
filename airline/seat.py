
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

    def __repr__(self):
        return "{\n" + ",\n".join( " {} : {}".format(repr(k),repr(v)) for k,v in vars(self).items()) + "\n}"

    def dict(self):
        if self._person:
            p = self._person.dict()
        else:
            p = None
        return { "flight_no" : self._flight_no,
                 "seat_no"   : self._seat_no,
                 "person"    : p,
                 "ts"        : self._ts}
