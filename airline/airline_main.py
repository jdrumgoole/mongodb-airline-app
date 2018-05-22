import pymongo
import pymongo.uri_parser
from collections import namedtuple

import argparse
from argparse import ArgumentParser

from airline.seatlog import SeatLog
from airline.flightlog import FlightLog

from airline.flight import Flight
from airline.person import Person
from airline.paymentlog import PaymentLog

if __name__ == "__main__":

    parser = ArgumentParser(formatter_class=argparse.MetavarTypeHelpFormatter)
    parser.add_argument("--host", default="mongodb://localhost:27017/MONGODB_AIR", type=str, help="Default MongoDB URI for connection")
    parser.add_argument("--addflight",nargs=3, metavar="a", type=str, help="Input 'flight no<str> no of seats<int> no of rows<int>" )
    parser.add_argument("--addperson",nargs=3, metavar="a", type=str, help="Input 'flight no<str> no of seats<int> no of rows<int>" )
    parser.add_argument("--init", default=False, action="store_true", help="Clear down databases and delete")
    parser.add_argument("--addseat", nargs=3, metavar="s", type=str, )
    args = parser.parse_args()


    client = pymongo.MongoClient(host=args.host)

    uri_dict = pymongo.uri_parser.parse_uri(args.host)

    if uri_dict["database"]:
        database_name = uri_dict["database"]
    else:
        database_name = "MONGODB_AIR"

    database = client[database_name]

    print( "Using database:'{}'".format(database_name))
    seats = SeatLog(database)
    payments = PaymentLog(database)
    flights = FlightLog(database)

    if args.init:
        print( "Dropping:'{}'".format(database_name))
        client.drop_database(database_name)
        seats.initialise()
        payments.initialise()

    FlightParams=namedtuple( "Flight", "flight_no seat_rows seat_width")

    if args.addflight:
        flight = FlightParams(*args.addflight)
        flight = Flight( flight.flight_no, int(flight.seat_rows), int(flight.seat_width))
        seats.add_flight(flight)


    PassengerParams=namedtuple( "Passenger", "first_name last_name DOB locator")

    if args.addperson:

        passenger = PassengerParams(*args.addperson)
        passenger = Person( passenger.first_name, passenger.last_name)
        passengers.add_person( flight_no=passenger.flight_no )
    if args.addseat:
        flights.add_flight()


    # buyer = Person( "Joe", "Drumgoole", "21-May-2000")
    # seat = seats.allocate_seat( flight.flight_no(), "1A", buyer )
    # payments.make_payment( buyer, seat, 500, "USD")