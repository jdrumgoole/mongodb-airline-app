import pymongo

from airline.flight import Flight
from airline.eventlog import EventLog
from datetime import datetime

class FlightLog(EventLog):
    """
    A Flight log is a record of all flight departures. A flight depature includes
    a flight number, a depature time and a depature date.
    """

    def __init__(self, database, collection_name="flight_log"):
        super().__init__(database, collection_name)

    def initialise(self):
        super().initialise()
        self._collection.create_index("flight_no")
        self._collection.create_index("departs")
        self._collection.create_index("ts")

    def add_flight(self, flight_no, time_and_date:datetime):

        self.insert_one( { 'flight_no': flight_no,
                           "departs"  : time_and_date,
                           "ts"       : datetime.utcnow()})