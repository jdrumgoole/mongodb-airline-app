import pymongo
from datetime import datetime
from airline.eventlog import EventLog

class PersonLog(EventLog):

    def __init__(self, database, collection_name="person_log"):

        super().__init__(database, collection_name)

    def initialise(self):
        super().initialise()
        self._collection.create_index("locator")
        self._collection.create_index("last_name")
        self._collection.create_index("ts")

    def get_person(self, person):
        return self.get_most_recent( { "locator" : person.locator})

    def add_person(self, person):

        if person._locator is not None:
            person["ts"] = datetime.utcnow()

        self.insert_one( person.dict())

    def find_person(self, locator):
        return self.find({"locator" })