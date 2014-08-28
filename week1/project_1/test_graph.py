from unittest import TestCase
from alg_module1_graphs import *
from graph_representation import Graph

__author__ = 'advena'


class TestGraph(TestCase):
    def setUp(self):
        self.instance = Graph()

    def test_make_complete_graph(self):
        complete_graph = GRAPH3
        graph_to_check = self.instance.make_complete_graph(5)
        self.assertEqual(complete_graph, graph_to_check)

    def test_compute_in_degrees(self):
        self.fail()

    def test_in_degree_distribution(self):
        self.fail()