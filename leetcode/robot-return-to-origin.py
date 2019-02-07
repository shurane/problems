class Solution:
    def judgeCircle(self, moves: 'str') -> 'bool':
        lr = 0
        ud = 0
        for letter in moves:
            if letter == "U":
                ud += 1
            elif letter == "D":
                ud -= 1
            elif letter == "L":
                lr -= 1
            else:
                lr += 1
        
        return lr == 0 and ud == 0
        
# 30 seconds