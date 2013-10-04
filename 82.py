from collections import defaultdict

class Cell(object):
    def __init__(self,row,col, data=None):
        self.row = row
        self.col = col
        self.data = data
        self.name = ""

    @classmethod
    def special(cls, name=""):
        cell = cls(-1,-1)
        cell.name = name
        return cell

    def __eq__(self, other):
        if self.row == other.row \
                and self.col == other.col \
                and self.name == other.name:
            return True
        return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __str__(self):
        return "Cell(row={0:2},col={1:2}{2}{3})".format(self.row,self.col,
                ",data={0}".format(self.data) if self.data else "",
                ",name={0}".format(self.name) if self.name else "")

class Matrix(object):
    def __init__(self,filename):
        self.matrix = []
        num_rows = 0
        iterator = (line.strip() for line in open(filename).readlines() if line.strip())
        for row_index, row in enumerate(iterator):
            row_line = []
            for col_index, cell in enumerate(row.split(",")):
                row_line.append(Cell(row_index,col_index,int(cell)))

            self.matrix.append(row_line)
            num_rows += 1

        num_cells = 0
        for cell in self.matrix[0]:
            num_cells += 1

        self.rows = num_rows
        self.cols = num_cells
        self.graph = defaultdict(set)

    def __str__(self):
        results = []
        for row in self.matrix:
            print_row = []
            for cell in row:
                print_row.append("{0:5}".format(cell))
            results.append(" ".join(print_row))
        return "\n".join(results)

    def __repr__(self):
        return str(self)

    def dimensions(self):
        return "{0}x{1}".format(m1.rows, m1.cols)

    def lookup(self,row,col):
        if self.valid_cell(row,col):
            return self.matrix[row][col]
        return None

    def valid_cell(self, row, col):
        if 0 <= row and row < self.rows and 0 <= col and col < self.cols:
            return True
        return False

    def add_edge(self, cell_a, cell_b):
        """doesn't add None elements"""
        if cell_b:
            self.graph[cell_a].add(cell_b)

    def lookup_edges(self, cell):
        return self.graph[cell]

    def create_graph(self):
        """graph of possible movements from any cell"""
        for row_index, row in enumerate(self.matrix):
            for col_index, col in enumerate(row):
                rowcol = self.lookup(row_index,col_index)

                # edges are absolute coordinates and are directed
                # adding edges above, below, and to the right of the cell
                for y in (-1,1):
                    cell = self.lookup(row_index+y,col_index)
                    self.add_edge(rowcol,cell)

                cell = self.lookup(row_index,col_index+1)
                self.add_edge(rowcol,cell)

        start = Cell.special("start")
        end = Cell.special("end")
        # add edge from start to self.matrix[*][0]
        # add edge from self.matrix[*][-1] to end
        for row_index, row in enumerate(self.matrix):
            cell = self.lookup(row_index, 0)
            self.add_edge(start, cell)

            cell = self.lookup(row_index, self.cols - 1)
            self.add_edge(cell, end)

        for k,v in self.graph.iteritems():
            print "Edges for {0}".format(k)
            for c in v:
                print "    {0}".format(c)

m1 = Matrix("matrix-easy.txt")
m1.create_graph()

