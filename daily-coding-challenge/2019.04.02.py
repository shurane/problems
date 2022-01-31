
"""
Question for 2019-04-02
[ 87 ] Asked by Dropbox

What does the below code snippet print out? How can we fix the anonymous functions to behave as we'd expect?
functions = []
for i in range(10):
    functions.append(lambda : i)

for f in functions:
    print(f())
"""

functions = []
for i in range(10):
    f = (lambda j: (lambda : j))(i)
    functions.append(f)

for f in functions:
    print(f())
