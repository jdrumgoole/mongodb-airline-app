
from airline.eventlog import EventLog
from airline.seat import Seat
from airline.person import Person
from enum import Enum


class SeatLog(EventLog):
    """
    Collection of all the seats allocated and unallocated on a set of planes
    """

    class Seat_Type(Enum):
        Free = 0
        Booked = 1

    def __init__(self, database, collection_name="seat_log"):
        super().__init__(database, collection_name)

    def add_flight(self, flight ):

        return self.insert_many(flight.dict())

    def allocate_seat(self, seat, person: Person) -> object:
        """
        :rtype: object
        """
        seat.allocate(person)
        self.insert_one( seat.dict())
        return seat


    def find_seats(self, flight_no, seat_type = Seat_Type.Free, limit=0):
        """

        :type seat_type: Enum
        """
        if seat_type is seat_type.Free:
            person_query = { "$eq" : None}
        else:
            person_query = { "$ne" : None }

        cursor = self._collection.find( {"flight_no": flight_no,
                                         "person" : person_query }).limit( limit )

        for i in cursor:
            yield Seat.make_seat(i)

    def deallocate_seat(self, seat):
        seat.deallocate()
        self.insert_one(seat.dict())
        return seat