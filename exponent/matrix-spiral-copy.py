from typing import List
from enum import Enum

class Direction(Enum):
  N = 1
  E = 2
  S = 3
  W = 4

# direction -> (y,x) coordinate
dir_map = {
  Direction.N: (-1,  0),
  Direction.E: ( 0,  1),
  Direction.S: ( 1,  0),
  Direction.W: ( 0, -1),
}

dir_next = {
  Direction.N: Direction.E,
  Direction.E: Direction.S,
  Direction.S: Direction.W,
  Direction.W: Direction.N,
}

def spiral_copy(inputMatrix: List[List[int]]) -> List[int]:
    result = []
    m = len(inputMatrix)
    n = len(inputMatrix[0])
    visited = [[False for j in range(n)] for i in range(m)]
    count = m * n
    y = 0
    x = 0
    d: Direction = Direction.E
    # print(f"initial: {m=}, {n=}")

    for i in range(count):
      result.append(inputMatrix[y][x])
      visited[y][x] = True

      # print(f"{i=}, {y=}, {x=}, {d=}")

      dy, dx = dir_map[d]
      ny = y + dy
      nx = x + dx
      # change directions
      if ny == -1 or ny == m or nx == -1 or nx == n or visited[ny][nx]:
        # print("changing directions, we hit a border",
        #     ny == -1, ny == m, nx == -1, nx == n, 0 <= ny < m and 0 <= nx < n and visited[ny][nx])
        d = dir_next[d]

      dy, dx = dir_map[d]

      y += dy
      x += dx

    return result

# debug your code below
inputMatrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(spiral_copy(inputMatrix))