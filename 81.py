
def read_matrix(filename):
    f = open(filename).read()
    matrix_str = f.strip().split("\n")
    matrix_int = []

    for row in matrix_str:
        row_int = [int(cell) for cell in row.split(",")]
        matrix_int.append(row_int)

    return matrix_int

def print_matrix(matrix, selected=[]):
    for row in matrix:
        for cell in row:
            print cell

matrix = read_matrix("matrix-easy.txt")
