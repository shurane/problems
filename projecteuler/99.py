import math

lines = open("base_exp.txt").readlines()
pairs = [map(int,line.strip().split(",")) for line in lines]
results = [ right * math.log(left) for left, right in pairs]
# list is 0-based, but file starts at line 1
print(results.index(max(results)) + 1)


