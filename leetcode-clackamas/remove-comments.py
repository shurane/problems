from typing import List

class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        output = []
        inBlockComment = False
        for line in source:
            remainder = line
            hasChanged = True

            if "*/" not in remainder and inBlockComment:
                remainder = ""

            while remainder and hasChanged:
                hasChanged = False

                if "/*" in remainder and "*/" in remainder:
                    left = remainder.find("/*")
                    right = remainder.find("*/")
                    remainder = remainder[:left] + remainder[right+2:] # len("*/")
                    hasChanged = True

                if "/*" in remainder:
                    idx = remainder.find("/*")
                    remainder = remainder[:idx]
                    inBlockComment = True
                    hasChanged = True

                if "*/" in remainder and inBlockComment:
                    idx = remainder.find("*/")
                    remainder = remainder[idx+2:] # len("*/")
                    inBlockComment = False
                    hasChanged = True

                if "//" in remainder:
                    idx = remainder.find("//")
                    remainder = remainder[:idx]
                    hasChanged = True

            # decide whether to append remainder to output depending on the length
            if remainder:
                print("remainder", remainder)
                output.append(remainder)



            # if "/*" in line and not inBlockComment:
                # print(1)
                # idx = line.find("/*")
                # remainder = line[:idx]
                # inBlockComment = True
            # elif inBlockComment: # empty out line since this is a comment
                # print(2)
                # remainder = ""
            # elif "*/" in line and inBlockComment:
                # print(3)
                # idx = line.find("*/")
                # remainder =  line[idx:]
                # inBlockComment = False
            # # line comment
            # elif "//" in line:
                # print(4)
                # idx = line.find("//")
                # remainder = line[:idx]
            # else: # just a regular programming line
                # print(5)
                # pass

            # if not inBlockComment and remainder:
                # output.append(remainder)

        print(output)
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

# assert s.removeComments(["/*only a block comment */"]) == []
# assert s.removeComments(["abc/*only a block comment */"]) == ["abc"]
# assert s.removeComments(["/*only a block comment */xyz"]) == ["xyz"]
# assert s.removeComments(i1) == o1
# assert s.removeComments([ "int main() { return 0; }// test comment" ]) == [ "int main() { return 0; }" ]

# TODO this is kind of tough without a stack of some kind -- maybe just convert inBlockComment into a stack
# why can't I just get a list of tokens instead of this strange line by line program? Should I just join it into one very large string?

assert s.removeComments(["a/*comment", "line", "more_comment*/b"]) == ["ab"]

# TODO multiple block comments on one line

