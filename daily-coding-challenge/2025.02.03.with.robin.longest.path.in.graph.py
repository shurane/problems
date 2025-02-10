from collections import defaultdict

def findLongest(edges: list[tuple[str, str]]):
    graph = defaultdict(list)
    for a, b in edges:
        graph[a].append(b)

    print("graph", graph)

    cache = {} # b:count

    def dfs(node: str):
        if node in cache:
            return cache[node]

        length = 1
        # set to 0 in case of cycles
        cache[node] = 0
        elements = graph[node] if node in graph else []
        for nextElem in elements:
            length = max(length, dfs(nextElem) + 1)

        cache[node] = length
        return length

    longest = 1
    for node in graph:
        longest = max(longest, dfs(node))
        print("longest for", node, dfs(node))

    return longest

lst1 = [("bob", "ross"),("yaris", "zack"), ("ross","kay"),("kay","io"), ("alice", "bob"), ("ross","jay"),("zack", "alice"), ("xyno", "yaris"), ("io", "ross"), ("","")]

print(findLongest(lst1))