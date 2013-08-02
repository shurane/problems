from common import bc
import sys

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
        self.cols = len(matrix_int[0])

    def print_2d(self, matrix=None, selected=[]):
        if matrix is None:
            matrix = self.matrix

        for rownum in xrange(self.rows):
            for colnum in xrange(self.cols):
                if (rownum,colnum) in selected:
                    print (bc.FAIL+"{0:4}"+bc.ENDC).format(matrix[rownum][colnum]),
                else:
                    print "{0:4}".format(matrix[rownum][colnum]),
            print

    def solve(self):

        ## oh boy, all this initialization...
        checked=set([(0,0)])
        queue=[(0,0)]
        path=[[0 for colnum in xrange(self.cols)]
                 for rownum in xrange(self.rows)]
        path[0][0] = self.matrix[0][0]

        while queue:
            #print "solve({0},{1})".format(rownum,colnum)
            #self.print_2d(selected=queue)

            rownum,colnum = queue.pop(0)

            def check_and_queue(rownum,colnum, checked, queue):
                rc = (rownum,colnum)
                if rc not in checked and \
                        (rownum < self.rows and colnum < self.cols):
                    queue.append(rc)
                    checked.add(rc)
                    # a bit ugly? doesn't follow the cleanliness of before
                    #print "{0:2},{1:2}".format(rownum-1, colnum-1)
                    left = path[rownum][colnum-1] if (colnum-1) >= 0 else sys.maxint
                    up = path[rownum-1][colnum] if (rownum-1) >= 0 else sys.maxint
                    path[rownum][colnum] = min(left,up) + self.matrix[rownum][colnum]

            check_and_queue(rownum+1, colnum,   checked, queue)
            check_and_queue(rownum  , colnum+1, checked, queue)
            check_and_queue(rownum+1, colnum+1, checked, queue)

        print path[-1][-1]
        #self.print_2d(matrix=path)

m1 = Matrix("matrix-easy.txt")
m1.solve()
m2 = Matrix("matrix.txt")
m2.solve()
