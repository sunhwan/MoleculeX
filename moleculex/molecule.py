import networkx as nx

class Molecule():
    """Molecule class"""

    def __init__(self):
        self.graph = nx.Graph()

    def add_atom(self, n):
        """Add a single atom"""

        self.graph.add_node(n)

    def add_bond(self, v, w):
        """Add a single bond"""

        self.graph.add_edge(v, w)

    def atoms(self):
        """Return a list of atoms"""

        return self.graph.nodes()

    def bonds(self):
        """Return a list of bonds"""

        return self.graph.edges()
