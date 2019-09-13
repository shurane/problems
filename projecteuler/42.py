from string import ascii_lowercase
from itertools import count, takewhile

def generate_triangle():
    for n in count(start=1):
        yield  (n * (n+1))/2

def translate(word):
    # probably some way to only evaluate this once, like returning a closure.
    alphamap = dict(zip(ascii_lowercase,range(1,27)))
    total = 0
    for char in word:
        total += alphamap[char.lower()]

    return total

words = open("words.txt").read().split(",")
words = [word.strip("\"") for word in words]

wordos = zip(map(translate,words),words)
topnum, topword = max(wordos)

g = generate_triangle()
triangles = takewhile(lambda number: number < topnum, g)
triangles = set(triangles)
triangles.add(g.next())
triangle_count = 0

for num, word in wordos:
    if num in triangles:
        triangle_count += 1

print(triangle_count)
