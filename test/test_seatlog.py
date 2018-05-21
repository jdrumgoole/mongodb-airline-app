import unittest
import pymongo
from airline.flight import Flight
from airline.seatlog import SeatLog
from airline.person import Person

class TestSeatLog(unittest.TestCase):

    def setUp(self):

        self._client = pymongo.MongoClient()
        self._database = self._client[ "TEST_SEATLOG"]
        self._log = SeatLog(self._database)
        self._log.initalise()

    def tearDown(self):
        pass

    def test_flight(self):

        f = Flight( "EI172", 50, Flight.six_seats)
        self._log.add_flight(f)
        seats = list( self._log.find_seats( "EI172", SeatLog.Seat_Type.Free))
        self.assertEqual(len(seats), 50 * len( Flight.six_seats))
        self._log.allocate_seat( seats[0], Person( "Joe", "Drumgoole", "1-May-2000"))

if __name__ == "__main__" :
    unittest.main()