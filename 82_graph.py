from common import bc
import sys

class Node(object):
    def __init__(self, weight):
        self.weight = weight
        self.edges = set()
        self.minpathsum = 0

    def add(self, other):
        if other in self.edges:
            print "{0} already connected to {1}".format(self,other)
        self.edges.add(other)

    def __str__(self):
        return "Node({0})".format(self.weight)
    def __repr__(self):
        return str(self)

class Matrix(object):
    def __init__(self, filename):
        f = open(filename).read()
        matrix_str = f.strip().split("\n")
        matrix_int = []

        for row in matrix_str:
            row_int = [Node(int(cell)) for cell in row.split(",")]
            matrix_int.append(row_int)

        self.matrix = matrix_int
        self.rows = len(matrix_int)
        self.cols = len(matrix_int[0])
        self.start_nodes = []
        self.end_nodes = []

        for rownum in xrange(self.rows):
            self.start_nodes.append(self.matrix[rownum][0])
            self.end_nodes.append(self.matrix[rownum][-1])

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
        pass


m1 = Matrix("matrix-easy.txt")
#m1.solve()
m1.print_2d(selected=[(3,3)])
print m1.matrix[3][3].weight
print m1.matrix[3][3].edges
