TODO:

- `rg "print "`
- `rg ":type"`
- `rg "Solution\(object"`
- `rg --files-without-match "assert"`

<!-- https://embeddedartistry.com/blog/2017/06/07/warnings-weverything-and-the-kitchen-sink/
     https://quuxplusone.github.io/blog/2018/12/06/dont-use-weverything/ -->
For Clang:
- `clang++ -Wall -Wextra -Wpedantic -Wno-unused-function filename.cpp && ./a.out`
- `clang++ -Weverything -Wno-c++98-compat -Wno-shadow-field-in-constructor -Wno-padded filename.cpp && ./a.out`
