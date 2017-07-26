from .element import Element

class Atom:
    """Atom"""

    name = None
    element = None

    def __init__(self, attr_dict=None, **kwargs):
        for k in kwargs:
            self.k = kwargs[k]

        if 'symbol' in kwargs or 'number' in kwargs:
            symbol = kwargs.get('symbol', None)
            number = kwargs.get('number', None)
            self.element = Element(symbol=symbol, number=number)
