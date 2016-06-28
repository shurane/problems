#include <iostream>
#include <vector>
#include <string>

bool inner_cell(int n, int y, int x){
    if (x > 0 && x < n-1 && y > 0 && y < n-1)
        return true;
    else
        return false;
}

bool is_cavity(std::vector<std::vector<int>>& matrix, int y, int x){
    if (inner_cell(matrix.size(), x, y)
        && matrix[y-1][x] < matrix[y][x]
        && matrix[y][x-1] < matrix[y][x]
        && matrix[y+1][x] < matrix[y][x]
        && matrix[y][x+1] < matrix[y][x])
        return true;
    else
        return false;
}

int main(int argc, char** argv){

    int n;
    std::cin >> n;
    std::cin.ignore(1000, '\n');

    std::vector<std::vector<int>> matrix(n);
    for (int i=0; i<n; i++){
        std::string l;
        std::vector<int> row(n);
        std::getline(std::cin, l);
        for (int j=0; j<n; j++){
            row[j] = l[j] - '0';
        }
        matrix[i] = row;
    }

    for (int i=0; i<n; i++){
        for (int j=0; j<n; j++){
            if (is_cavity(matrix, i, j))
                std::cout << 'X';
            else
                std::cout << matrix[i][j];
        }
        std::cout << std::endl;
    }

}
