from .element import Element

class Atom:
    """Atom"""

    name = None
    element = None

    def __init__(self, attr_dict=None, **kwargs):
        for k in kwargs:
            setattr(self, k, kwargs[k])

        if 'symbol' in kwargs:
            self.element = Element(symbol=self.symbol)
        elif 'name' in kwargs:
            symbol = self.name[0]
            self.element = Element(symbol=symbol)
