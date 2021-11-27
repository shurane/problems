from typing import Dict, List, Tuple

class TimeMap:

    def __init__(self):
        self.d: Dict[str, List[Tuple[int, str]]] = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.d:
            self.d[key] = []

        self.d[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.d:
            return ""

        lst = self.d[key]

        if timestamp < lst[0][0]:
            return ""

        lo = 0
        hi = len(lst) - 1
        while lo < hi:
            mid = (lo + hi) // 2
            # print(f"lo:{lo}, hi:{hi}, mid:{mid}", lst[mid])
            if timestamp < lst[mid][0]:
                hi = mid - 1
            elif timestamp > lst[mid][0]:
                lo = mid + 1
            else: #elif timestamp >= lst[mid][0]:
                lo = mid
                hi = mid

        # print(f"reached end, lo:{lo}, hi:{hi}", lst[lo])
        if timestamp < lst[lo][0]:
            lo = lo - 1
        return lst[lo][1]

s = TimeMap()
s.set("foo", "bar", 1)
# assert s.get("foo", 1) == "bar"
# assert s.get("foo", 3) == "bar"
s.set("foo", "bar4", 4)
assert s.get("foo", 4) == "bar4"
assert s.get("foo", 5) == "bar4"

s1 = TimeMap()
s.set("a", "1", 1)
s.set("a", "2", 2)
s.set("a", "4", 4)
s.set("a", "5", 5)
s.set("a", "6", 6)
s.set("a", "8", 8)
s.set("a", "9", 9)
s.set("a", "15", 15)

assert s.get("a", 1) == "1"
assert s.get("a", 2) == "2"
assert s.get("a", 3) == "2"
assert s.get("a", 4) == "4"
assert s.get("a", 5) == "5"
assert s.get("a", 6) == "6"
assert s.get("a", 7) == "6"
assert s.get("a", 8) == "8"
assert s.get("a", 9) == "9"
assert s.get("a", 10) == "9"
assert s.get("a", 11) == "9"
assert s.get("a", 12) == "9"
assert s.get("a", 13) == "9"
assert s.get("a", 14) == "9"
assert s.get("a", 15) == "15"
assert s.get("a", 16) == "15"