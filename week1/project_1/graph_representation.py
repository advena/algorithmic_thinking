EX_GRAPH0 = {0: set([1, 2]),
             1: set([]),
             2: set([])}

EX_GRAPH1 = {0: set([1, 4, 5]),
             1: set([2, 6]),
             2: set([3]),
             3: set([0]),
             4: set([1]),
             5: set([2]),
             6: set([])}

EX_GRAPH2 = {0: set([4, 1]),
             1: set([2, 6]),
             2: set([3, 7]),
             3: set([7]),
             4: set([1]),
             5: set([2]),
             6: set([]),
             7: set([3]),
             8: set([1, 2]),
             9: set([0, 4, 5, 6, 7, 3])}


class Graph():
    """
    Graph representation
    """

    def __init__(self):
        self.graph = {}


    def make_complete_graph(self, num_nodes):
        """
        Creates complete graph from given nodes that every node is conected to every node with no selfloops
        """
        return {}


    def compute_in_degrees(self, digraph):
        """

        """

        return {}

    def in_degree_distribution(self, digraph):
        """

        """
        return {}
