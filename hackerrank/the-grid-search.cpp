#include <iostream>
#include <vector>
#include "prettyprint.hpp"

std::vector<std::vector<int>> readmatrix(int r, int c){
    std::vector<std::vector<int>> rows(r);
    for (int ri=0; ri<r; ri++){
        std::vector<int> row(c);
        std::string row_as_string;
        std::getline(std::cin, row_as_string);
        for (int i=0; i<row_as_string.size(); i++){
            // lol ascii
            row[i] = row_as_string[i] - '0';
        }
        rows[ri] = row;
    }
    return rows;
}

// starts at (y,x) for a total of r rows and c columns
std::vector<std::vector<int>> submatrix(
        std::vector<std::vector<int>> matrix,
        int y, int x,
        int r, int c){
    std::vector<std::vector<int>> sub(r);
    for (int i=y; i<y+r; i++){
        std::vector<int> sub_row(c);
        for (int j=x; j<x+c; j++){
            sub_row[j-x] = matrix[i][j];
        }
        sub[i-y] = sub_row;
    }
    return sub;
}

bool matches2(std::vector<std::vector<int>>& a, int y, int x, int r, int c, std::vector<std::vector<int>>& pattern){
    for (int i=y; i<y+r; i++){
        for (int j=x; j<x+c; j++){
            if (a[i][j] != pattern[i-y][j-x])
                return false;
        }
    }
    return true;
}

bool matches(std::vector<std::vector<int>>& a, std::vector<std::vector<int>>& b){
    if (a.size() != b.size())
        return false;
    else if (a[0].size() > 0 &&
             b[0].size() > 0 &&
             a[0].size() != b[0].size())
        return false;
    else {
        for (int i=0; i<a.size(); i++){
            for (int j=0; j<a[0].size(); j++){
                if (a[i][j] != b[i][j])
                    return false;
            }
        }
        return true;
    }
}

int main(int argc, char** argv){
    int  t;
    std::cin >> t;
    //std::cout << "num cases: " << t << std::endl;

    for (int i=0; i<t; i++){
        int r;
        int c;
        std::cin >> r;
        std::cin >> c;
        std::cin.ignore(1000, '\n');
        //std::cout << "r: " << r << ", c: " << c << std::endl;
        auto rows = readmatrix(r, c);

        int pr;
        int pc;
        std::cin >> pr;
        std::cin >> pc;
        std::cin.ignore(1000, '\n');
        //std::cout << "pr: " << pr << ", pc: " << pc << std::endl;
        auto pattern = readmatrix(pr, pc);

        //// rows are set up, now to find submatrix that matches
        //std::cout << "grid:" << std::endl;
        //for (auto it= rows.begin(); it!=rows.end(); it++){
            //std::cout << *it << std::endl;
        //}
        //std::cout << "pattern:" << std::endl;
        //for (auto it= pattern.begin(); it!=pattern.end(); it++){
            //std::cout << *it << std::endl;
        //}

        bool found_match = false;
        for (int j=0; j<r-pr+1; j++){
            for (int k=0; k<c-pc+1; k++){

                //for (auto it=subm.begin(); it!=subm.end(); it++){
                    //std::cout << *it << std::endl;
                //}
                //std::cout << "===========" << std::endl;

                // wow, making this many vectors is *SLOW*
                //auto subm = submatrix(rows, j, k, pr, pc);
                //if (matches(subm, pattern)){

                if (matches2(rows, j, k, pr, pc, pattern)){
                    //std::cout << submatrix(rows, j, k, pr, pc) << std::endl;
                    found_match = true;
                }
            }
        }

        if (found_match)
            std::cout << "YES" << std::endl;
        else
            std::cout << "NO" << std::endl;

    }
}
