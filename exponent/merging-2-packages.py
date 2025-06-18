# this is just two-sum from leetcode
# https://www.tryexponent.com/practice/prepare/merging-2-packages

from typing import List

def get_indices_of_item_weights(arr: List[int], limit: int) -> List[int]:
    seen = {}
    for i, weight in enumerate(arr):
        remaining = limit - weight
        if remaining in seen:
            return [i, seen[remaining]]

        seen[weight] = i

    return []