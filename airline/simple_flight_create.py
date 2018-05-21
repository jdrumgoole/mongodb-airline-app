import pymongo

from airline.seatlog import SeatLog
from airline.flight import Flight
from airline.person import Person
from airline.paymentlog import PaymentLog

if __name__ == "__main__":
    client = pymongo.MongoClient()
    database = client["MONGODB_AIR"]

    # make a flight with 70 rows, 6 seats per row
    seats = SeatLog(database)
    payments = PaymentLog(database)

    flight = Flight( "EI179", 70, ["A", "B", "C", "D", "E", "F"])

    seats.add_flight(flight)

    buyer = Person( "Joe", "Drumgoole", "21-May-2000")
    seat = seats.allocate_seat( flight.flight_no(), "1A", buyer )
    payments.make_payment( buyer, seat, 500, "USD")