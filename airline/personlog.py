from airline.eventlog import EventLog

class PersonLog(EventLog):

    def __init__(self, database, collection_name="person_log"):

        super().__init__(database, collection_name)

    def initialise(self):
        super().initialise()
        self._collection.create_index("locator", unique=True)
        self._collection.create_index("last_name")

    def add_person(self, person):
        self.insert_one( person.dict())

    def find_person(self, locator):
        return self.find({"locator" })