from typing import List

class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        output = []
        remainder = ""
        iterable = iter(source)
        while iterable:
            try:
                remainder = next(iterable)
                hasChanged = True
            except StopIteration:
                break

            while remainder and hasChanged:
                # print("while loop", remainder)
                hasChanged = False

                # TODO this shouldn't match "/* ... // ... */" because then it won't close the comment correctly
                left =  remainder.find("/*")
                right = remainder.find("*/", 0 if left < 0 else left + 2)
                linecomment = remainder.find("//")

                # if "//" in remainder and not hasChanged:
                if linecomment >= 0 and left < 0:
                    remainder = remainder[:linecomment]
                    hasChanged = True

                if "/*" in remainder and "*/" in remainder:
                    left = remainder.find("/*")
                    right = remainder.find("*/", left+2) #len("/*")
                    remainder = remainder[:left] + remainder[right+2:] # len("*/")
                    hasChanged = True

                if "/*" in remainder:
                    left = remainder.find("/*")
                    print("before", remainder)
                    while remainder.find("*/", left+2) == -1:
                        print("during", remainder)
                        remainder = remainder + "\\n" + next(iterable)
                    hasChanged = True

            # decide whether to append remainder to output depending on the length
            if remainder:
                # print("remainder", remainder)
                output.append(remainder)

        # print(output)
        return output

s = Solution()

i1 = [ "/*Test program */"
     , "int main()"
     , "{ "
     , "  // variable declaration "
     , "int a, b, c;"
     , "/* This is a test"
     , "   multiline  "
     , "   comment for "
     , "   testing */"
     , "a = b + c;"
     , "}"]
o1 = ["int main()"
     ,"{ "
     ,"  "
     ,"int a, b, c;"
     ,"a = b + c;"
     ,"}"]
i2 = ["struct Node{", "    /*/ declare members;/**/", "    int size;", "    /**/int val;", "};"]
o2 = ["struct Node{","    ","    int size;","    int val;","};"]
i3 = ["main() {", "/* here is commments", "  // still comments */", "   double s = 33;", "   cout << s;", "}"]
o3 = ["main() {", "   double s = 33;", "   cout << s;", "}"]
i4 = ["void func(int k) {", "// this function does nothing /*", "   k = k*2/4;", "   k = k/2;*/", "}"]
o4 = ["void func(int k) {","   k = k*2/4;","   k = k/2;*/","}"]

assert s.removeComments(["/*only a block comment */"]) == []
assert s.removeComments(["abc/*only a block comment */"]) == ["abc"]
assert s.removeComments(["/*only a block comment */xyz"]) == ["xyz"]
assert s.removeComments([ "int main() { return 0; }// test comment" ]) == [ "int main() { return 0; }" ]
assert s.removeComments(["a/*comment", "line", "more_comment*/b"]) == ["ab"]
assert s.removeComments(i1) == o1
assert s.removeComments(i2) == o2
assert s.removeComments(i3) == o3
assert s.removeComments(i4) == o4

# TODO should I use a stack instead?
# why can't I just get a list of tokens instead of this strange line by line program? Should I just join it into one very large string?

# TODO 2021/04/03 still a WIP
