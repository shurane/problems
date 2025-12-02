# https://stackoverflow.com/questions/4122831/disable-make-builtin-rules-and-variables-from-inside-the-make-file
.SUFFIXES:

# https://embeddedartistry.com/blog/2017/06/07/warnings-weverything-and-the-kitchen-sink/
# https://quuxplusone.github.io/blog/2018/12/06/dont-use-weverything/
# https://stackoverflow.com/questions/20738232/gcc-4-9-undefined-behavior-sanitizer
CXXFLAGS=-std=c++20 -g -Wall -Wextra -Wpedantic -Wno-unused-function -Wno-sign-compare -fsanitize=address -fsanitize=undefined

# https://stackoverflow.com/questions/40621451/makefile-automatically-compile-all-c-files-keeping-o-files-in-separate-folde
SOURCES := $(wildcard *.cpp)
OBJECTS := $(patsubst %.cpp, %.elf, $(SOURCES))

%.elf: %.cpp
	$(CXX) $(CXXFLAGS) $< -o $@

%.run: %.elf
	./$<

all: $(OBJECTS)

clean:
	rm -f $(OBJECTS)

#EXECUTABLES := $(wildcard *.elf)
#run: $(EXECUTABLES)
#make -j4 all
