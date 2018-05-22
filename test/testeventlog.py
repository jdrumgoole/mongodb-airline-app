import pymongo
import unittest

from datetime import datetime

from airline.eventlog import EventLog



class MyTestCase(unittest.TestCase):

    def setUp(self):
        self._c=pymongo.MongoClient()
        self._db=self._c["TEST_EVENTLOG"]


    def tearDown(self):
        self._c.drop_database(self._db)

    def test_eventlog(self):
        self._eventlog = EventLog( self._db)
        self._eventlog.initialise()

        doc = self._eventlog.get_most_recent({"hello" : "world"})
        self.assertEqual( doc, None)
        ts = datetime.utcnow()
        doc = self._eventlog.insert_one( {"hello" : "world"})
        self.assertGreaterEqual( doc["ts"], ts)
        doc = self._eventlog.get_most_recent({"hello" : "world"})

if __name__ == '__main__':
    unittest.main()
