from common import bc

class Matrix(object):
    def __init__(self, filename):
        f = open(filename).read()
        matrix_str = f.strip().split("\n")
        matrix_int = []

        for row in matrix_str:
            row_int = [int(cell) for cell in row.split(",")]
            matrix_int.append(row_int)

        self.matrix = matrix_int
        self.rows = len(matrix_int)
        self.columns = len(matrix_int[0])

    def print_matrix(self, selected=[]):
        for rownum in xrange(self.rows):
            for columnnum in xrange(self.columns):
                if (rownum,columnnum) in selected:
                    print (bc.FAIL+"{0:4}"+bc.ENDC).format(self.matrix[rownum][columnnum]),
                else:
                    print "{0:4}".format(self.matrix[rownum][columnnum]),
            print

matrix = Matrix("matrix-easy.txt")
matrix.print_matrix(selected=[(1,1),(2,2)])
