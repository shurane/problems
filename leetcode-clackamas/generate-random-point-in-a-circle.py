from typing import List
import random
import math

class Solution:
    def __init__(self, radius: float, x_center: float, y_center: float):
        self.radius = radius
        self.x_center = x_center
        self.y_center = y_center

    def randPoint(self) -> List[float]:
        # create a polar coordinate with a random angle
        # then convert it into rectangular coordinates
        # follow up by translating it using (x_center, y_center)

        # notes after wrong submission
        # apparently r needs to be generated randomly between (0,radius)
        # see https://leetcode.com/problems/generate-random-point-in-a-circle/discuss/1113679/Python-Polar-coordinates-explained-with-diagrams-and-math
        angle = random.uniform(0, math.pi * 2)
        r = self.radius * math.sqrt(random.random())
        x = r * math.cos(angle)
        y = r * math.sin(angle)
        return [self.x_center + x, self.y_center + y]

obj =  Solution(1, 0, 0)
for i in range(10):
    print(obj.randPoint())