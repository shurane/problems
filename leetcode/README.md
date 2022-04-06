TODO:

```bash
rg "print "
rg ":type"
rg "Solution\(object"
rg --files-without-match "assert"
```

C++:

```bash
# https://embeddedartistry.com/blog/2017/06/07/warnings-weverything-and-the-kitchen-sink/
# https://quuxplusone.github.io/blog/2018/12/06/dont-use-weverything/
# https://stackoverflow.com/questions/20738232/gcc-4-9-undefined-behavior-sanitizer
CPPFLAGS="-Wall -Wextra -Wpedantic -Wno-unused-function -Wno-c++17-extensions -fsanitize=address -fsanitize=undefined"
clang++ $CPPFLAGS filename.cpp && ./a.out
```
