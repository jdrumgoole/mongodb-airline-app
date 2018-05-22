class Person(object):

    def __init__(self, first_name: str=None, last_name: str=None, DOB: str=None, locator=None):
        self._first_name = first_name
        self._last_name = last_name
        self._DOB = DOB
        self._locator = locator

    def dict(self):
        return {"first_name": self._first_name,
                "last_name": self._last_name,
                "DOB": self._DOB,
                "locator" : self._locator}