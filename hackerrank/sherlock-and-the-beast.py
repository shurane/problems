import sys

t = int(sys.stdin.readline())
numbers = [int(sys.stdin.readline()) for i in range(t)]

def splitto3sand5s(n):
	max3s = n / 5
	max5s = n / 3
	i = max5s
	# how to make this more readable?
	while i > 0:
		digits_left = n - (3 * i)
		if digits_left % 5 == 0:
			return [i*3, digits_left]
		i -= 1
	if n % 5 == 0:
		return [0, n]
	else:
		return [-1, -1]

# either 3 fives or 5 threes
for n in numbers:
	threes, fives = splitto3sand5s(n)
	if threes == -1:
		print "-1"
	else:
		s = ""
		s += "5" * threes
		s += "3" * fives
		print s
