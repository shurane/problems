from common import bc
import sys
import collections
from functools import total_ordering

class Node(object):
    def __init__(self, weight):
        self.weight = weight
        self.edges = set()

    def add(self, other):
        # A->B is B->A. undirected edges.
        self.edges.add(other)
        other.edges.add(self)

    def __str__(self):
        return "Node({0})".format(self.weight)
    def __repr__(self):
        return str(self)

class Graph(object):
    def __init__(self, nodes=set()):
        self.nodes = nodes

    def add_node(self, node):
        prev_size = len(self.nodes)
        self.nodes.add(node)
        next_size = len(self.nodes)
        if next_size == prev_size:
            print("not a new node!")

    def unconnected_nodes(self):
        nodes = set()
        for node in self.nodes:
            if len(node.edges) == 0:
                nodes.add(node)
        return nodes

class Matrix(object):
    def __init__(self, filename):
        f = open(filename).read()
        self.graph = Graph()
        matrix_str = f.strip().split("\n")
        matrix_int = []

        for row in matrix_str:
            row_int = []
            for cell in row.split(","):
                node = Node(int(cell))
                self.graph.add_node(node)
                row_int.append(node)
            matrix_int.append(row_int)

        self.matrix = matrix_int
        self.rows = len(matrix_int)
        self.cols = len(matrix_int[0])
        self.start_nodes = []
        self.end_nodes = []
        self.actual_start = Node(0)
        self.actual_end = Node(0)
        self.graph.add_node(self.actual_start)
        self.graph.add_node(self.actual_end)

        for rownum in xrange(self.rows):
            self.start_nodes.append(self.matrix[rownum][0])
            self.end_nodes.append(self.matrix[rownum][-1])

        for node in self.start_nodes:
            self.actual_start.add(node)

        for node in self.end_nodes:
            node.add(self.actual_end)

        for colnum in xrange(self.cols):
            for rownum in xrange(self.rows):
                current = self.matrix[rownum][colnum]
                top = self.matrix[rownum-1][colnum] if rownum-1 >= 0 else None
                bottom = self.matrix[rownum+1][colnum] if rownum+1 < self.rows else None
                right = self.matrix[rownum][colnum+1] if colnum+1 < self.cols else None

                if top: current.add(top)
                if bottom: current.add(bottom)
                if right: current.add(right)

    def print_2d(self, selected=[]):

        for rownum in xrange(self.rows):
            for colnum in xrange(self.cols):
                if (rownum,colnum) in selected:
                    print (bc.FAIL+"{0:4}"+bc.ENDC).format(self.matrix[rownum][colnum].weight),
                else:
                    print "{0:4}".format(self.matrix[rownum][colnum].weight),
            print

    def solve(self):
        start = self.actual_start
        end = self.actual_end

        # working with Dijkstra's algorithm
        # http://www.cs.auckland.ac.nz/software/AlgAnim/dijkstra.html
        D = {}      # final distances
        P = {}      # predecessors
        Q = {}      # estimated non-final distances
        D[start] = 0
        VS = self.graph.nodes.difference(set([start]))
        VS = reachable(start)

        while VS:
            currentVS = sorted(VS, key=lambda self: self.weight)
            closest = currentVS.pop(0)
            print closest


            VS = set(currentVS)

def reachable(subgraph = set(), n=1):
    """returns nodes that are n degrees away from a subgraph"""
    # when subgraph = one node
    if not isinstance(subgraph, collections.Iterable):
        subgraph = set([subgraph])

    reached = set()
    for node in subgraph:
        for node2 in node.edges:
            reached.add(node2)
    if n > 1:
        reached.update(reachable(reached, n-1))
    return reached


m1 = Matrix("matrix-easy.txt")
#m1.print_2d(selected=[(3,3)])

m1.solve()
