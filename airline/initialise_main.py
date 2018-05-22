import pymongo
import argparse
from argparse import ArgumentParser

from airline.flightlog import FlightLog
from airline.seatlog import SeatLog
from airline.paymentlog import PaymentLog
from airline.personlog import PersonLog

if __name__ == "__main__" :
    parser = ArgumentParser(formatter_class=argparse.MetavarTypeHelpFormatter)
    parser.add_argument("--host", default="mongodb://localhost:27017/MONGODB_AIR", type=str,
                        help="Default MongoDB URI for connection")

    args = parser.parse_args()

    client = pymongo.MongoClient(args.host)

    uri_dict = pymongo.uri_parser.parse_uri(args.host)

    if uri_dict["database"]:
        database_name = uri_dict["database"]
    else:
        database_name = "MONGODB_AIR"

    database = client[database_name]

    print( "Using database:'{}'".format(database_name))

    print( "Initalising collections")
    flights =FlightLog(database)
    flights.initialise()
    print("'{}.{}'initalised".format( database_name, flights.name()))
    seats = SeatLog(database)
    seats.initialise()
    print("'{}.{}'initalised".format( database_name, seats.name()))
    payments =PaymentLog(database)
    payments.initialise()
    print("'{}.{}'initalised".format( database_name, payments.name()))
    passengers = PersonLog(database)
    passengers.initialise()
    print("'{}.{}'initalised".format( database_name, passengers.name()))
