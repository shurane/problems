def decrypt(word: str) -> str:
    leftover = 1
    result = ""
    A_VAL = ord('a')
    for c in word:
        val = ord(c)
        nextLeftover = val
        val -= leftover

        while (val < A_VAL):
            val += 26
        # if (val < A_VAL):
        #     m = (97 - val) // 26
        #     val += m*26


        result += chr(val)
        leftover = nextLeftover

    return result

# debug your code below
print(decrypt("dnotq"))

"""

dnotq

d 100 99
n 110 - 100 -> 10 36 62 88 114
o 111 - 110 -> 1 27 53 79 105
t 116 - 111 -> 5 31 57 83 109

"""