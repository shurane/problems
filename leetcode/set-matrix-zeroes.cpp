#include <vector>
#include <iomanip>
#include <iostream>
#include <assert.h>
using namespace std;

void initMatrix(vector<vector<int>>& matrix, int m, int n){
    int count = 1;
    for (int i=0; i<m; i++){
        for (int j=0; j<n; j++){
            matrix[i][j] = count++;
        }
    }
}
void printMatrix(std::ostream& out, vector<vector<int>>& matrix, string message = "", char fill=' ', int width=0){
    int last = matrix[0].size() - 1;
    out << message << std::endl;
    for (auto row: matrix) {
        out << "{";
        for (int i = 0; i < row.size(); i++){
            out << std::setfill(fill) << std::setw(width) << row[i];
            if (i != last)
                out << ", ";
        }
        out << "}" << std::endl;
    }
    out << std::endl;
}

class Solution {
public:
    void setZeroes(vector<vector<int>>& matrix) {
        int m = matrix.size();
        int n = matrix[0].size();
        int i, j;

        bool firstCol = false;
        bool firstRow = false;

        for (i=0; i<m; i++){
            for (j=0; j<n; j++){
                if (matrix[i][j] == 0){
                    if (i == 0) firstRow = true;
                    if (j == 0) firstCol = true;
                    matrix[i][0] = 0;
                    matrix[0][j] = 0;
                }
            }
        }

        for (i=1; i<m; i++){
            if (matrix[i][0] == 0){
                for (j=1; j<n; j++){
                    matrix[i][j] = 0;
                }
            }
        }

        for (j=1; j<n; j++){
            if (matrix[0][j] == 0){
                for (i=1; i<m; i++){
                    matrix[i][j] = 0;
                }
            }
        }

        if (firstRow){
            for (j=0; j<n; j++){
                matrix[0][j] = 0;
            }
        }
        if (firstCol){
            for (i=0; i<m; i++){
                matrix[i][0] = 0;
            }
        }
    }
};

int main()
{
    Solution s;
    for (int n=1; n<10; n++){
        vector<vector<int>> matrix(n, vector<int>(n));

        {
            initMatrix(matrix, n, n);
            printMatrix(cout, matrix, "initial", ' ', 2);

            s.setZeroes(matrix);

            // no value in the matrix should be zero
            for (int i=0; i<n; i++)
                for (int j=0; j<n; j++)
                    assert(matrix[i][j] != 0);
        }

        {
            initMatrix(matrix, n, n);

            // odd rows are set to zero, also the first column
            for (int i=1; i<n; i+=2)
                matrix[i][0] = 0;
            printMatrix(cout, matrix, "odd rows to 0, first column to 0, before", ' ', 2);

            s.setZeroes(matrix);
            printMatrix(cout, matrix, "odd rows to 0, first column to 0, after", ' ', 2);

            // first column is all zeroes
            if (n > 1){
                for (int i=0; i<n; i++){
                    assert(matrix[i][0] == 0);
                }
            }

            for (int i=1; i<n; i++){
                for (int j=0; j<n; j++){
                    if (i%2 == 0 && j != 0)
                        assert(matrix[i][j] != 0);
                    else
                        assert(matrix[i][j] == 0);
                }
            }
        }

        {
            initMatrix(matrix, n, n);

            // odd columns are set to zero, also the first row
            for (int j=1; j<n; j+=2)
                matrix[0][j] = 0;
            printMatrix(cout, matrix, "odd columns to 0, first row to 0, before", ' ', 2);

            s.setZeroes(matrix);
            printMatrix(cout, matrix, "odd columns to 0, first row to 0, after", ' ', 2);

            // first row is all zeroes
            if (n > 1){
                for (int j=0; j<n; j++){
                    assert(matrix[0][j] == 0);
                }
            }

            for (int i=1; i<n; i++){
                for (int j=0; j<n; j++){
                    if (j%2 == 0 && i != 0)
                        assert(matrix[i][j] != 0);
                    else
                        assert(matrix[i][j] == 0);
                }
            }
        }

        {
            initMatrix(matrix, n, n);

            for (int i=0; i<n; i++)
                matrix[i][i] = 0;
            printMatrix(cout, matrix, "main diagonal to 0, before", ' ', 2);

            s.setZeroes(matrix);
            printMatrix(cout, matrix, "main diagonal to 0, after", ' ', 2);

            // all values in the matrix should be zero
            for (int i=0; i<n; i++)
                for (int j=0; j<n; j++)
                    assert(matrix[i][j] == 0);

        }

        {
            initMatrix(matrix, n, n);

            for (int i=0; i<n; i++)
                matrix[n-i-1][i] = 0;
            printMatrix(cout, matrix, "antidiagonal to 0, before", ' ', 2);

            s.setZeroes(matrix);
            printMatrix(cout, matrix, "antidiagonal to 0, after", ' ', 2);

            // all values in the matrix should be zero
            for (int i=0; i<n; i++)
                for (int j=0; j<n; j++)
                    assert(matrix[i][j] == 0);

        }

    }
}

