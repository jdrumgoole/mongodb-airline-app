import pymongo
from datetime import datetime

class EventLog(object):

    def __init__(self, database, collection_name="event_log"):
        self._database = database
        self._collection_name = collection_name
        self._collection = self._database[self._collection_name]

    def initialise(self):
        self.drop()
        self._collection = self._database[self._collection_name]

    def name(self):
        return self._collection_name

    def insert_one(self, doc):
        doc["ts"] = datetime.utcnow()
        self._collection.insert_one(doc)
        return doc

    def insert_many(self, docs):

        for i in docs:
            i["ts"] = datetime.utcnow()

        return self._collection.insert_many(docs)

    def get_most_recent(self, doc):
        cursor= self._collection.find(doc).sort("ts", pymongo.DESCENDING).limit(1)
        for i in cursor:
            return i
        return None

    def get_history(self, doc):
        cursor= self._collection.find(doc).sort("ts", pymongo.DESCENDING)
        for i in cursor:
            yield i

    def drop(self):
        return self._collection.drop()