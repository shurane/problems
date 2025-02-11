from string import ascii_lowercase
from pprint import pprint

def lower_and_remove_punctuation(s: str):
    return "".join(c for c in s.lower() if c in ascii_lowercase)

def word_count_engine(document: str) -> list[list[str]]:
    wordmap: dict[str, tuple[int,int]] = dict()

    for i, word in enumerate(document.split(" ")):
        normalized_word = lower_and_remove_punctuation(word)
        if normalized_word not in wordmap:
            wordmap[normalized_word] = (1,i)
        else:
            a,b = wordmap[normalized_word]
            wordmap[normalized_word] = (a+1, b)

    if "" in wordmap:
        del wordmap[""]

    def keyfn(item: tuple[str, tuple[int,int]]) -> tuple[int, int]:
        count = item[1][0]
        index = item[1][1]
        return (-count, index)

    def to_str(item: tuple[str, tuple[int,int]]) -> list[str]:
        return [item[0], str(item[1][0])]

    values = list(map(to_str, sorted(wordmap.items(), key=keyfn)))
    # pprint(values)

    return values

s1 = "Practice makes perfect. you'll only get Perfect by practice. just practice!"
s2 = 'Every book is a quotation; and every      house is a quotation out of all forests, and mines,  and stone quarries; and every man is a quotation from all his ancestors. '

assert(word_count_engine(s1) == [
    ['practice', '3'],
    ['perfect', '2'],
    ['makes', '1'],
    ['youll', '1'],
    ['only', '1'],
    ['get', '1'],
    ['by', '1'],
    ['just', '1']
])


assert(word_count_engine(s2) == [
    ['and', '4'],
    ['every', '3'],
    ['is', '3'],
    ['a', '3'],
    ['quotation', '3'],
    ['all', '2'],
    ['book', '1'],
    ['house', '1'],
    ['out', '1'],
    ['of', '1'],
    ['forests', '1'],
    ['mines', '1'],
    ['stone', '1'],
    ['quarries', '1'],
    ['man', '1'],
    ['from', '1'],
    ['his', '1'],
    ['ancestors', '1']
])
