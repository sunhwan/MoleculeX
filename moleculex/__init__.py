"""
MoleculeX
=========
    MoleculeX (MX) is a Python package for the creation, manipulation, and
    study of the structure, dynamics, and functions of complex molecules.
Using
-----
    Just write in Python
    >>> import moleculex as mx
    >>> G=mx.Molecule()
    >>> G.add_bond(1,2)
    >>> G.add_atom(42)
    >>> print(sorted(G.atoms()))
    [1, 2, 42]
    >>> print(sorted(G.bonds()))
    [(1, 2)]
"""

import moleculex.classes
from moleculex.classes import *

