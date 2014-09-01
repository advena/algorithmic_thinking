from netrc import netrc
from pytz.reference import first_sunday_on_or_after
from unittest import TestCase
from alg_module1_graphs import *
import alg_module1_graphs
from graph_representation import Graph

__author__ = 'advena'


class TestGraph(TestCase):
    def setUp(self):
        self.instance = Graph()

    def test_make_complete_graph(self):
        #given
        complete_graph = GRAPH3
        #then
        graph_to_check = self.instance.make_complete_graph(5)
        #finally
        self.assertEqual(complete_graph, graph_to_check)

    def test_make_complete_graph_for_non_positive_number_of_nodes(self):
        #given
        graph_to_check = {}
        #then
        zero_nodes_graph = self.instance.make_complete_graph(0)
        negative_nodes_graph = self.instance.make_complete_graph(-1)
        #finally
        self.assertEqual(zero_nodes_graph, graph_to_check)
        self.assertEqual(negative_nodes_graph, graph_to_check)


    def test_compute_in_degrees(self):
        #given
        expected_output = {0: 4, 1: 0, 2: 0, 3: 0, 4: 0}
        first_graph = alg_module1_graphs.GRAPH1
        #then
        output = self.instance.compute_in_degrees(first_graph)
        #finally
        self.assertEqual(expected_output, output)


    def test_in_degree_distribution(self):
        #given
        expected_output = {1: 4}
        first_graph = alg_module1_graphs.GRAPH0
        #then
        output = self.instance.in_degree_distribution(first_graph)
        #finally
        self.assertEqual(expected_output, output)
