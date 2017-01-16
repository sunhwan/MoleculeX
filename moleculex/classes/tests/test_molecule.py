from moleculex import Molecule
from moleculex import Atom
import pytest

def test_atom():
    a = Atom()
    assert a.atomic_number == 0
    # test set attribute
    b = Atom(1)
    a.atomic_number = 1
    assert a.atomic_number == b.atomic_number
    # test updating attribute
    with pytest.raises(Exception):
        a.atomic_number = 119

def test_add_atom():
    G = Molecule()
    # test add attributes
    a = Atom(1)
    b = Atom(2)
    c = Atom(3)
    G.add_atom(a)
    G.add_atom(b)
    G.add_atom(c)
    assert G.atom[0].atomic_number == 1
    assert G.atom[1].atomic_number == 2
    assert G.atom[2].atomic_number == 3
