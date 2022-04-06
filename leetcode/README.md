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
$CPPFLAGS="-Wall -Wextra -Wpedantic -Wno-unused-function -fsaanitize=address -Wno-c++17-extensions"
clang++ $CPPFLAGS filename.cpp && ./a.out
```
