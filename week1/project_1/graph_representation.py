from to_coursera import compute_in_degrees

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
        Takes the number of nodes num_nodes and returns a dictionary corresponding to a complete directed graph with
        the specified number of nodes. A complete graph contains all possible edges subject to the restriction that
        self-loops are not allowed. The nodes of the graph should be numbered 0 to num_nodes - 1 when num_nodes is
        positive. Otherwise, the function returns a dictionary corresponding to the empty graph.
        """
        if num_nodes <= 0:
            return {}
        nodes = [x for x in range(0, num_nodes)]
        graph = {}
        for node in nodes:
            graph[node] = set([x for x in range(num_nodes) if x != node])

        return graph

    def compute_in_degrees(self, digraph):
        """
        Takes a directed graph digraph (represented as a dictionary) and computes the in-degrees for the nodes in the
        graph. The function should return a dictionary with the same set of keys (nodes) as digraph whose corresponding
        values are the number of edges whose head matches a particular node.
        """

        nodes = digraph.keys()
        graph = {x: 0 for x in nodes}
        for node in nodes:
            for edge in digraph[node]:
                graph[edge] += 1

        return graph


    def in_degree_distribution(self, digraph):
        """
        Takes a directed graph digraph (represented as a dictionary) and computes the unnormalized distribution of the
        in-degrees of the graph. The function should return a dictionary whose keys correspond to in-degrees of nodes
        in the graph. The value associated with each particular in-degree is the number of nodes with that in-degree.
        In-degrees with no corresponding nodes in the graph are not included in the dictionary.
        """

        in_degrees = compute_in_degrees(digraph)
        output = {}
        for value in in_degrees.values():
            current_key = value
            if output.has_key(current_key):
                output[current_key] += 1
            else:
                output[current_key] = 1

        return output
