"""Base class for molecules.
The molecule class allows an atom object as a node
and can associate key/value attribute pairs with each bond.
"""

class Molecule(object):
    """
    Base class for molecules.
    """

    atom = {}

    def __init__(self):
        self._atom_idx_counter = 0
        pass

    def add_atom(self, atom):
        self.atom[self._atom_idx_counter] = atom
        self._atom_idx_counter += 1
