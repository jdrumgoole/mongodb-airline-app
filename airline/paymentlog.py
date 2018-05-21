
from datetime import datetime
from airline.eventlog import EventLog
from airline.person import Person

class Payment(object):

    def __init__(self, person, item, amount, currency ):
        self._amount   = amount
        self._currency = currency
        self._item     = item
        self._person   = person

    def dict(self):
        return {"amount"   : self._amount,
                "currency" : self._currency,
                "item"     : self._item.dict(),
                "person"   : self._person.dict()}



class PaymentLog(EventLog):

    def __init__(self, database, collection_name="payment_log"):
        super().__init__(database, collection_name)

    def initalise(self):
        super().initialise()
        self.make_payment( Person(), { "status:Initalised"},None, None)
        self._collection.create_index( {"ts":1})
        self._collection.create_index( {"person":1})
        self._collection.create_index( {"item":1})
        self._collection.create_index( {"person":1})


    def make_payment(self, person, item, amount, currency ):
        #
        # Contact payment processor here.
        #
        self.insert_one( { "amount"   : amount,
                           "currency" : currency,
                           "item"     : item.dict(),
                           "person"   : person.dict(),
                           "ts"       : datetime.utcnow()})

    def find_payment(self, amount=None, item=None, person=None ):

        query={}
        if amount:
            query["amount"] = amount
        if item:
            query[ "item"] = item
        if person:
            query["person"] = person

        return self._collection.find(query)

