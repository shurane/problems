from blessings import Terminal
t = Terminal()

lines = open("./67.txt").readlines()
#lines = open("./18.txt").readlines()
#lines = open("./18-easy.txt").readlines()

numbers = []
sumsofar = []
for line in lines:
    number_line = map(int, line.strip().split())
    numbers.append(number_line)
    sumsofar.append([0 for number in number_line])

for i in xrange(len(numbers)):
    for j in xrange(len(numbers[i])):
        print '{: 3d}'.format(numbers[i][j]),
        if i-1 < 0:
            # base case
            sumsofar[i][j] = numbers[i][j]
        else:
            up_left = 0
            # really it's the upper left one
            up_right = 0

            if j < len(numbers[i-1]):
                up_left = sumsofar[i-1][j]
            if j-1 < len(numbers[i-1]):
                up_right = sumsofar[i-1][j-1]

            print t.red('{: 3d} {: 3d}'.format(up_left, up_right)),
            sumsofar[i][j] = max(up_left, up_right) + numbers[i][j]
    print

for l in sumsofar:
    for elem in l:
        print '{: 3d}'.format(elem),
    print

print(max(sumsofar[-1]))
