"""Base class for atoms.
"""

class Atom(object):
    """
    Base class for atom.
    """

    _atomic_number = 0

    def __init__(self, number=None):
        if number is not None:
            self._atomic_number = number

    @property
    def atomic_number(self):
        return self._atomic_number

    @atomic_number.setter
    def atomic_number(self, number):
        if number <= 118 and number >= 0:
            self._atomic_number = number
        else:
            raise Exception("Invalid atomic number")
